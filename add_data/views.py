import re
import requests
from django.shortcuts import render, redirect
from django.views import View
from .form import QuestionForm, AnswerForm
from .models import Answer, Question


class AddDataToDb(View):

    def get(self, request):
        question_form = QuestionForm()
        context = {
            'question_form' : question_form,
        }
        return render(request, 'add_data.html', context)


    def post(self, request):
        question_form = QuestionForm(request.POST)
        answer_list = [value for key, value in request.POST.items() if re.search('answer\d+', key)]
        if question_form.is_valid():
            q_obj = question_form.save()
        for aswer_obj in answer_list:
            answer_obj = Answer(question=q_obj, answer=aswer_obj)
            answer_obj.save()
        context = {
            'question_form' : question_form,
        }
        return render(request, 'add_data.html', context)


class ListData(View):

    def get(self, request):
        print request.META
        question = Question.objects.all()
        question_lis = []
        for ob in question:
            dic_obj = {
                'question' : ob.text,
                'type' : ob.type,
                'created_at' : ob.created_at,
                'answer_obj' : Answer.objects.filter(question=ob.id)
            }
            question_lis.append(dic_obj)
        context = {
            'question_lis' : question_lis,
        }
        return render(request, 'list_data.html', context)


class GetMyIp(View):

    def get(self, request):
        text = requests.get('http://ipv4.whatismyv6.com/')
        return render(request, 'ip.html', {'text' : text.content})