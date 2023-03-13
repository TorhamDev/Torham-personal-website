from django.urls import path
from mentoring.views import MentoringPage

urlpatterns = [
    path('', MentoringPage.as_view(), name="mentoring-page"),
]
