
from django.urls import include, path
from . import views



urlpatterns = [
    path('uploadfile/',views.uploadFile, name='userUpload'),
]