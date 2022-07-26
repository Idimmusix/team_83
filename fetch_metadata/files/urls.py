
from django.urls import include, path
from . import views



urlpatterns = [
    path('',views.fileListView.as_view(), name='userFileList'),
    path('class/',views.fileCreateView.as_view(), name='userFileUpload'),
]