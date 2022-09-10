
from django.urls import path
from . import views

urlpatterns = [
    path('',views.seller_login,name='login'),
    path('index/',views.seller_index,name='index'),
]