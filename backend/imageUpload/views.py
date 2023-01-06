import numpy as np
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
    
    # def  


class ImageDisplayView(generics.ListAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = UploadImageSerializers
    
class ImageDetailView(generics.RetrieveAPIView):
    
    queryset = ImageUpload.objects.all()
    serializer_class= UploadImageSerializers
    lookup_field = 'pk'
    

# for image_batch, label_batch in dataset.take(1):
#     first_image = image_batch[0].numpy().astype('uint8')
#     first_label = label_batch[0].numpy()

#     print("first image to predict")
#     plt.imshow(first_image)
#     print(f'actual label is {class_names[first_label]}')

#     batch_predict = model.predict(image_batch)
#     predict_label = np.argmax(batch_predict[0])
#     print(f"predicted label is {class_names[predict_label]}")
#     plt.axis("off")


