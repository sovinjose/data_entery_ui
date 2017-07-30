import re
import requests
from django.shortcuts import render, redirect
from django.views import View
from .form import QuestionForm, AnswerForm, TaskForm, AspirationForm
from .models import Answer, Question, Task, Membership, Aspiration, TaskAspirationMapping


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
        return redirect('/list')


class AddAspirationToDb(View):

    def get(self, request):
        task_form = AspirationForm()
        context = {
            'task_form' : task_form,
        }
        return render(request, 'newdata.html', context)

    def post(self, request):
        print ">>>>>>>>>>>>>>>>", request.POST
        task_ids = request.POST.getlist('task')
        task_name = request.POST.get('name')
        if task_ids and task_name:
            task_obj = Aspiration.objects.create(name=task_name)
            for task in task_ids:
                t_obj = Task.objects.get(id=task)
                m = TaskAspirationMapping.objects.create(aspiration=task_obj, task=t_obj)
                m.save()
        return redirect('/aspiration/%s/preference' % (task_obj.id))


class AddAspirationPreferenceView(View):

    def get(self, request, pk):
        t = Aspiration.objects.get(id=pk)
        mem = TaskAspirationMapping.objects.filter(aspiration=t)
        dic_obj = {
                'id' : t.id,
                'question' : t.name,
                'answer_obj' : mem,
                'l' : range(1,len(mem)+1)
            }
        return render(request, 'aspiration_preference.html', dic_obj)

    def post(self, request, pk):
        d = request.POST.items()
        for key, value in d:
            if key !='csrfmiddlewaretoken':
                mem = TaskAspirationMapping.objects.get(id=key)
                mem.preference = value
                mem.save()
        return redirect('/aspiration/list')


class AddAspirationListData(View):

    def get(self, request):
        t = Aspiration.objects.all()
        question_lis = []
        for ob in t:
            mem = TaskAspirationMapping.objects.filter(aspiration=ob)
            dic_obj = {
                'id' : ob.id,
                'question' : ob.name,
                'answer_obj' : mem,
                'l' : range(len(mem))
            }
            question_lis.append(dic_obj)
        context = {
            'question_lis' : question_lis,
        }
        return render(request, 'aspiration_list_data.html', context)



class AddTaskToDb(View):

    def get(self, request):
        task_form = TaskForm()
        context = {
            'task_form' : task_form,
        }
        return render(request, 'task_data.html', context)

    def post(self, request):

        question_ids = request.POST.getlist('question')
        task_name = request.POST.get('name')
        print question_ids, task_name
        if question_ids and task_name:
            task_obj = Task.objects.create(name=task_name)
            for question_id in question_ids:
                q_obj = Question.objects.get(id=question_id)
                m = Membership.objects.create(question=q_obj, task=task_obj)
                m.save()
        return redirect('/add/%s/preference' % (task_obj.id))


class AddPreferenceView(View):

    def get(self, request, pk):
        t = Task.objects.get(id=pk)
        mem = Membership.objects.filter(task=t)
        dic_obj = {
                'id' : t.id,
                'question' : t.name,
                'answer_obj' : mem,
                'l' : range(1,len(mem)+1)
            }
        return render(request, 'preference.html', dic_obj)

    def post(self, request, pk):
        d = request.POST.items()
        for key, value in d:
            if key !='csrfmiddlewaretoken':
                mem = Membership.objects.get(id=key)
                mem.preference = value
                mem.save()
        return redirect('/task/list')

      
class TaskListData(View):

    def get(self, request):
        t = Task.objects.all()
        question_lis = []
        for ob in t:
            mem = Membership.objects.filter(task=ob)
            dic_obj = {
                'id' : ob.id,
                'question' : ob.name,
                'answer_obj' : mem,
                'l' : range(len(mem))
            }
            question_lis.append(dic_obj)
        context = {
            'question_lis' : question_lis,
        }
        return render(request, 'task_list_data.html', context)


class ListData(View):

    def get(self, request):
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