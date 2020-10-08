from django.urls import path, include 
from . import views 

urlpatterns = [
    path('',views.index,name = "index"),
    path(r'customer/',views.customer,name = "customer"),
    path('movie/',views.movie,name = "movie")
    ]