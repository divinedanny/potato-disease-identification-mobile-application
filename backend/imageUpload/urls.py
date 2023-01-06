from django.urls import path
from .views import ImageDetailView, ImageDisplayView, ImageView


urlpatterns = [
    path('', ImageView.as_view(), name='upload'),
    path('history', ImageDisplayView.as_view(), name='history'),
    path('history/<int:pk>/', ImageDetailView.as_view(),name='detail')
]