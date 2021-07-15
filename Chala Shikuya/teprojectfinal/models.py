import pickle
import cv2
import tensorflow as tf
from keras.models import load_model as lm1
from keras.models import model_from_json
from sklearn.svm import SVC

# Use pickle to load in the pre-trained model.
def return_loaded_model():
        json_file = open('teprojectfinal/static/models/model2.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        #load weights into new model
        loaded_model.load_weights("teprojectfinal/static/models/model2.h5")
        print("Loaded Model from disk")
        #compile and evaluate loaded model
        loaded_model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        return loaded_model

def return_loaded_model2():
        json_file = open('teprojectfinal/static/models/modelletter.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model2 = model_from_json(loaded_model_json)
        #load weights into new model
        loaded_model2.load_weights("teprojectfinal/static/models/modelletter.h5")
        print("Loaded Model from disk")
        #compile and evaluate loaded model
        loaded_model2.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        return loaded_model2

def return_loaded_model3():
        json_file = open('teprojectfinal/static/models/nhcd_vowel_canvas.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model3 = model_from_json(loaded_model_json)
        #load weights into new model
        loaded_model3.load_weights("teprojectfinal/static/models/nhcd_vowel_canvas.h5")
        print("Loaded Model from disk")
        #compile and evaluate loaded model
        loaded_model3.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        return loaded_model3