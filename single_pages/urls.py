from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home), #홈페이지 대문주소
    path('', views.landing),
]