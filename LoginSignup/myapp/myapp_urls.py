from myapp import views
from django.urls import path

urlpatterns = [
    path('signup/', views.user_signup),
    path('login/', views.user_login),
    path('home/', views.Home),
    path('logout/', views.user_logout)
]