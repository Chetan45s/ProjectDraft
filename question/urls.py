from django.urls import path
from .views import GetQuestionsApi,GetAllDocuments

urlpatterns = [
    path('getAllDocuments/',GetAllDocuments.as_view(),name="GetDocuments"),
    path('getQuestions/<int:documentID>', GetQuestionsApi.as_view(), name="GetQuestions"),
]