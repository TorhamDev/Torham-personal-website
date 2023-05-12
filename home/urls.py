from django.urls import path
from home import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index-page"),
    path('about/', views.AboutView.as_view(), name="about-page"),
]
