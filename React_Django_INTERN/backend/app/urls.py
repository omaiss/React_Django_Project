from django.urls import path
from app import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    
]
