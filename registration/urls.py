from django.urls import path
from . import views

urlpatterns = [
    path('',views.registerFunction,name='signup'),
    path('login/',views.loginFunction, name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout')
]
