from dataclasses import fields
from .models import ImageUpload
from rest_framework import serializers


class UploadImageSerializers(serializers.ModelSerializer):
    image_url = serializers.ImageField(required = True)
    
    class Meta:
        model = ImageUpload
        fields = ['id','image_url','prediction_text','prediction_percentage']
        

            

