from django.urls import path
from .views import GetQuestionsApi

urlpatterns = [
    path('getQuestions/<int:documentID>', GetQuestionsApi.as_view(), name="GetQuestions"),
]