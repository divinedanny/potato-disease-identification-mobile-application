import django
from django.urls import path
from .views import index, predictImage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='upload'),
    path('predict', predictImage, name='predict'),
    # path('history/<int:pk>/', ImageDetailView.as_view(),name='detail')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

