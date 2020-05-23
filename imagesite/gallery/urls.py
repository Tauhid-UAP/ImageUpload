from django.urls import path
from . import views

# app_name='imagesite'

urlpatterns = [

    path('', views.view_gallery, name='view_gallery'),

]