from flask import Flask, render_template, url_for, redirect, request,flash
from teprojectfinal import app,db,bcrypt,mail
from teprojectfinal.predict import *
from teprojectfinal.forms import *
from teprojectfinal.data import *
from flask_login import login_user,current_user,logout_user,login_required
from playsound import playsound
from flask_mail import Message

def send_reset_email(u):
    token = u.get_reset_token()
    msg = Message('Password Reset Request',sender='siddheshbhere@gmail.com', recipients = [u.email])
    msg.body = f'''To reset your password,visit the following link:
{url_for('reset_token',token=token,_external=True)}

If you did not make this request then simply ignore this email and no changes will be made  
'''
    mail.send(msg)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/regilog",methods=['GET','POST'])
def regilog():
    form = RegiForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            u = user(username=form.username.data,email=form.email.data,contact=form.phone.data,password=hashed_password)
            db.session.add(u)
            db.session.commit()
            flash('You account was successfully created')
            return redirect(url_for('regilog'))
        
    return render_template("regilog.html",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = RegiForm()
    if request.method == 'POST':
        username = request.form['namel']
        password = request.form['passwordl']
        
        u = user.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password,password):
            login_user(u)
            next_page = request.args.get('next')
            return redirect(url_for(next_page)) if next_page else redirect(url_for('t2'))
        else:
            flash('invalid username or password \n please sign in to continue')
            
    return render_template('regilog.html',form=form)

@app.route("/request_password",methods=['GET','POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        u = user.query.filter_by(email=form.email.data).first()
        send_reset_email(u)
        flash('an email has been sent with instructions to reset your password')
        return redirect(url_for('regilog'))
    return render_template('reset.html',form=form)

@app.route("/request_password/<token>",methods=['GET','POST'])
def reset_token(token):
    u = user.verify_reset_token(token)
    if u is None:
        flash('That is an invalid or expired token')
        return redirect(url_for('reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        u.password = hashed_password
        db.session.commit()
        flash('Your password was updated succesfully')
        return redirect(url_for('regilog'))

    return render_template('reset_token.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/t1")
@login_required
def t1():
    return render_template('t1.html')

@app.route("/t2")
@login_required
def t2():
    return render_template('t2.html')

@app.route("/tut0")
@login_required
def tut0():
	return render_template('tut0.html')

@app.route("/tut0b")
@login_required
def tut0b():
    return render_template('tut0b.html')

@app.route("/v1")
@login_required
def v1():
    return render_template('v1.html')

@app.route("/v1b")
@login_required
def v1b():
    return render_template('v1b.html')

@app.route("/v2")
@login_required
def v2():
    return render_template('v2.html')

@app.route("/tut1")
@login_required
def tut1():
    return render_template('tut1.html')

@app.route("/tut1b")
@login_required
def tut1b():
    return render_template('tut1b.html')

@app.route("/tut2")
@login_required
def tut2():
    return render_template('tut2.html')

@app.route("/can/<int:v1>/<int:v2>",methods=['GET','POST'])
@login_required
def can(v1,v2):
    if request.method == 'POST':
        
        i,final_pred =predict(v1,v2) 

        if v2==100 and i==12 or v2==1 and i==0 or v2==2 and i==1 or v2==3 and i==2 or v2==4 and i==3 or v2==5 and i==4 or v2==6 and i==5 or v2==7 and i==6 or v2==8 and i==7 or v2==9 and i==8 or v2==10 and i==9 or v2==11 and i==10 or v2==12 and i==11 or v2==13 and i==1 or v2==14 and i==2 or v2==15 and i==3 or v2==16 and i==4 or v2==17 and i==5 or v2==18 and i==6 or v2==19 and i==7 or v2==20 and i==8 or v2==21 and i==9 or v2==22 and i==10 or v2==23 and i==11 or v2==24 and i==12 or v2==25 and i==13 or v2==26 and i==14 or v2==27 and i==15 or v2==28 and i==16 or v2==29 and i==17 or v2==30 and i==18 or v2==31 and i==19 or v2==32 and i==20 or v2==33 and i==21 or v2==34 and i==22 or v2==35 and i==23 or v2==36 and i==24 or v2==37 and i==25 or v2==38 and i==26 or v2==39 and i==27 or v2==40 and i==28 or v2==41 and i==29 or v2==42 and i==30 or v2==43 and i==31 or v2==44 and i==32 or v2==45 and i==33 or v2==46 and i==34 or v2==47 and i==35 or v2==48 and i==36 or v2==49 and i==0 or v2==50 and i==1 or v2==51 and i==2 or v2==52 and i==3 or v2==53 and i==4 or v2==54 and i==5 or v2==55 and i==6 or v2==56 and i==7 or v2==57 and i==8 or v2==58 and i==9:
            playsound('teprojectfinal/static/audios/RightAns.mp3')
            flash("उत्तर बरोबर आहे   -   "+ final_pred)
        else:
            playsound('teprojectfinal/static/audios/WrongAns.mp3')
            flash("उत्तर चुकीचे आहे")

        return render_template("can.html",v1=v1,v2=v2)

    else:
        return render_template('can.html',v1=v1,v2=v2)

@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

@app.errorhandler(Exception)
def exception_handler(error):
    return "!!!!"  + repr(error)
