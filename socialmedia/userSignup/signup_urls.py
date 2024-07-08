from userSignup import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signUp),
    path('login/', views.userLogin)
]