from unicodedata import name
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('handlesignup', views.handlesignup, name="handlesignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('handlelogout', views.handlelogout, name="handlelogout"),
    path('uploadproduct', views.uploadproduct, name="uploadproduct"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('deleteproduct/<int:pk>', views.deleteproduct, name="deleteproduct"),
    path('productlist', views.productlist, name="productlist"),
    path('productdetails/<int:pk>', views.productdetails, name="productdetails"),
    path('search', views.search, name="search"),
    path('about', views.about, name="about"),
    path('pro', views.pro, name="pro"),
   
   
   
    
  
    
   

    
    
    
]
