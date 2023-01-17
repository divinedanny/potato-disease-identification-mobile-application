from distutils.core import run_setup
from unittest import result
import cv2
import numpy as np
from .models import ImageUpload
from .serializers import UploadImageSerializers
from rest_framework import generics
from rest_framework.views import APIView
import tensorflow as tf
from .apps import *
from django.shortcuts import render
from django.core.files.storage import default_storage
from keras.preprocessing import image
from keras import layers


# Create your views here.

    
def index(request):
    context={"a":1}
    return render(request, 'index.html', context)


image_size = 256
def predictImage(request):
    # if request.method == 'POST':
    class_names = ['Potato___Early_blight',
                   'Potato___Late_blight', 'Potato___healthy']
    print(request)
    print(request.POST.dict())
    # print(request.FILES['filepath'])
    file = request.FILES['filepath'].file
    fs = default_storage
    filepathName = fs.save("temp.jpg", file)
    filepathName = fs.url(filepathName)
    
    #predicting image
    imageClassifier = ImageuploadConfig.model
    with default_storage.open("temp.jpg") as f:
        img = cv2.imread(f.name)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = img/255
        img = cv2.resize(img,(image_size,image_size))
        img = np.expand_dims(img, axis=0)
        
        
        result = imageClassifier.predict(img)
        result = np.argmax(result)
        result = class_names[result]
        print(result)
    
    # img = image.load_img(testimage, target_size=(image_size,image_size))
    
    
    
    
    context = {'filepathName': filepathName, 'result':result}
    return render(request, 'index.html', context)
    