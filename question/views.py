from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import *
import json
# Create your views here.

QuestionModels = [
    'TextQuestion',
    'ConditionalQuestion',
    'BooleanQuestion',
    'DateQuestion',
    'OptionalQuestion',
    'AddressQuestion'
]


class GetQuestionsApi(views.APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("documentID")
        Questions = []

        
        text = TextQuestion.objects.filter(Document=pk)
        condition = ConditionalQuestion.objects.filter(Document=pk)
        boolean = BooleanQuestion.objects.filter(Document=pk)
        date = DateQuestion.objects.filter(Document=pk)
        optional = OptionalQuestion.objects.filter(Document=pk)
        address = AddressQuestion.objects.filter(Document=pk)
        for ques in text:
            Questions.append(ques.getQuestion())
        for ques in condition:
            Questions.append(ques.getQuestion())
        for ques in boolean:
            Questions.append(ques.getQuestion())
        for ques in date:
            Questions.append(ques.getQuestion())
        for ques in optional:
            Questions.append(ques.getQuestion())
        for ques in address:
            Questions.append(ques.getQuestion())

            # print(json.dumps(ques.getQuestion()))

        sortedListOfQuestions = sorted(Questions, key=lambda d: d['Question Number']) 



        return Response({"Message" : "Request Submitted","Data":sortedListOfQuestions})
