from teprojectfinal.models import *
from teprojectfinal.img_pro import *
from flask import request

#Initialize the useless part of the base64 encoded image.
init_Base64 = 21;

#Our dictionary
anka = {0:'०', 1:'१', 2:'२', 3:'३', 4:'४', 5:'५',6:'६',7:'७',8:'८',9:'९'}
vyanjan = {10:'ञ',11:'ट ',12:'ठ',13:'ड',14:'ढ',15:'ण',16:'त',17:'थ',18:'द',19:'ध',1:'क',20:'न',21:'प',22:'फ',23:'ब',24:'भ',25:'म',26:'य',27:'र',28:'ल',29:'व',2:'ख',30:'श',31:'ष',32:'स',33:'ह',34:'क्ष',35:'त्र',36:'ज्ञ',3:'ग',4:'घ',5:'ङ',6:'च',7:'छ',8:'ज',9:'झ'}
swar = {10:'औ',11:'अं',12:'अः',13:'ऋ',1:'अ',2:'आ',3:'इ',4:'ई',5:'उ',6:'ऊ',7:'ए',8:'ऐ',9:'ओ'}

#Initializing the Default Graph (prevent errors)
graph = tf.compat.v1.get_default_graph()

def predict(v1,v2):
    if v1 == 1:
        final_pred = None
        #Access the image
        draw = request.form['url']
        #Removing the useless part of the url.
        draw = draw[init_Base64:]
        te_image  = b64_str_to_np(draw)
        #cv2.imwrite('static/images/b64decode.jpg',te_image)
        te_image1 = crop_img(te_image,v1)
        #cv2.imwrite('static/images/crop.jpg',te_image1)
        te_image2 = center_img(te_image1)
        #cv2.imwrite('static/images/center.jpg',te_image2)
        te_image3 = resize_img(te_image2,v1)
        te_image3 = 255 - te_image3
        cv2.imwrite('teprojectfinal/static/imagesswar/13/60.jpg',te_image3)
        te_image4 = reshape_array((te_image3),v1)
        #cv2.imwrite('static/images/reshape.jpg',te_image4)
        te_image5 = te_image4.astype('float32')
        te_image5 = te_image5/255
        #cv2.imwrite('static/images/final.jpg',te_image5)
        my_prediction = return_loaded_model3().predict(te_image5)
        #Getting the index of the maximum prediction
        i = my_prediction.argmax()
        #Associating the index and its value within the dictionnary
        final_pred = swar[i+1]
    else:
        global graph
        with graph.as_default():
            final_pred = None
            #Access the image
            draw = request.form['url']
            #Removing the useless part of the url.
            draw = draw[init_Base64:]
            te_image  = b64_str_to_np(draw)
            #cv2.imwrite('static/images/b64decode.jpg',te_image)
            te_image1 = crop_img(te_image,v1)
            #cv2.imwrite('static/images/crop.jpg',te_image1)
            te_image2 = center_img(te_image1)
            #cv2.imwrite('static/images/center.jpg',te_image2)
            te_image3 = resize_img(te_image2,v1)
            #cv2.imwrite('static/images/resize.jpg',te_image3)
            te_image4 = reshape_array(te_image3,v1)
            #cv2.imwrite('static/images/reshape.jpg',te_image4)
            te_image5 = te_image4.astype('float32')
            te_image5 = te_image5/255
            #cv2.imwrite('static/images/final.jpg',te_image5)
                    
            if v1 == 3:
                my_prediction = return_loaded_model().predict(te_image5)
                i = my_prediction.argmax()
                final_pred = anka[i]
            else:
                my_prediction = return_loaded_model2().predict(te_image5)
                i = my_prediction.argmax()
                final_pred = vyanjan[i]
	
    return i,final_pred
