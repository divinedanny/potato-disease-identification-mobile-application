from pyexpat import model
from django.db import models


# Create your models here.
def Image(instance, filename):
    return f'image/{filename}'


class ImageUpload(models.Model):
    image_url = models.ImageField(upload_to=Image)
    prediction_text = models.TextField(blank=True, null=True)
    prediction_percentage = models.TextField(max_length=10, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prediction_text

