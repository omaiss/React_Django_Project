from django.urls import path
from app import views

urlpatterns = [
    path('userview/', views.UserList.as_view()),
    path('useradd/', views.UserAdd.as_view()),
    path('userverify/', views.VerifyOTP.as_view()),
    path('resendotp/', views.Resend_OTP.as_view()),
    path('userlogin/', views.UserLogin.as_view()),
    path('customuseradd/', views.CustomUserAdd.as_view()),
]
