from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
	path('',  views.myindex ,name='index'),
	path('donation', views.donation, name='donation')

 ]