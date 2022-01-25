from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('forgetp/',views.forgetp,name='forgetp'),
    #path('forgetadminpass/',views.forgetadminpass,name='forgetadminpass'),
    path('twolink/',views.twolink,name='twolink'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
   # path('adminchange/',views.adminchange,name='adminchange'),
   # path('otp/',views.otp,name='otp'),
   path('howi/',views.howi,name='howi'),
   path('changepassword/<token>/',views.changepassword,name='changepassword'),
]