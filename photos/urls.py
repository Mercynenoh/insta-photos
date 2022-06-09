from django.urls import path
from . import views
urlpatterns = [
    path('image/<str:pk>', views.viewPhoto, name='image'),
    path('followers_count/', views.followers_count, name='followers_count'),

]