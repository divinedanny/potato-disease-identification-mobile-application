from django.shortcuts import render
from .models import ImageUpload
from .serializers import UploadImageSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.
# @api_view()['POST']
class ImageView(generics.CreateAPIView):
    queryset = ImageUpload.objects.order_by('-created')
    serializer_class = UploadImageSerializers
    parser_classes = (MultiPartParser, FormParser)

    # def create(request, serializer):
    #     serializer.save()

