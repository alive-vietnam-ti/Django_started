from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('get-contact/', views.getContact, name='getContact'),
]
