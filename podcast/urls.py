from django.urls import path
from podcast import views

app_name = 'podcast'
urlpatterns = [
    path('', views.PodcastList.as_view(), name="list"),
]
