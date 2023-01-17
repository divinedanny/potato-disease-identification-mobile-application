from django.apps import AppConfig
from django.conf import settings
import joblib
import os
from keras.models import load_model
import json



image_size = 32
# with open(os.path.join)




class ImageuploadConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "imageUpload"
    # MODEL_FILE = os.path.join(
    #     settings.MODEL, "potato_disease_prediction_work_2.pkl")
    # model = joblib.load(MODEL_FILE)
    
    model = load_model(os.path.join(
    settings.MODEL, "potato_disease_prediction_work_2.h5"))
