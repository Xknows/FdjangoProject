from django.urls import path
from . import views

urlpatterns = [
    path("hello/",views.sayHello),
    path("bay/",views.sayBay)
]