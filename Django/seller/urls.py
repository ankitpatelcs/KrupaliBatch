
from django.urls import path
from . import views

urlpatterns = [
    path('',views.seller_login,name='login'),
    path('index/',views.seller_index,name='index'),
    path('addproduct/',views.seller_addproduct,name='addproduct'),
    path('manageproduct/',views.manageproduct,name='manageproduct'),
]