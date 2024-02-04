
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='shophome'),
    path('about',views.about,name='about'),
    path('shop/product/<int:myid>',views.productview,name='productview'),
    path('shop/checkout',views.checkout,name='checkout'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('signup_data',views.signup_data,name='signup_data'),
    path('signin_data',views.signin_data,name='signin_data'),
    path('shop/Order',views.Order,name='Order'),
]