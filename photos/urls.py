from django.urls import path
from . import views
urlpatterns = [
    path('image/<str:pk>', views.viewPhoto, name='image'),

]