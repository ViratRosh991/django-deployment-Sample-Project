#SampleApp2/urls.py - File

from django.urls import path
from SampleApp2 import views

urlpatterns = [
	path("three/",views.f33),
	path("four/",views.f44)
];