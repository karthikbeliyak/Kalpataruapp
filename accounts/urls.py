from django.urls import path,re_path
from . import views
 

urlpatterns = [
    path('register/', views.register_view ,name='register'),
]