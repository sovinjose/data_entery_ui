import re
import requests
from django.shortcuts import render, redirect
from django.views import View
from .form import QuestionForm, AnswerForm, TaskForm, AspirationForm, SkillForm, NotificationForm
from .models import Answer, Question, Task, Membership, Aspiration, TaskAspirationMapping, AspirationSkillMapping, Skill
#from backup import s


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
        return redirect('/answer/%s/preference' % (q_obj.id))


class AnswerPrefernce(View):

    def get(self, request, q_id):
        print ">>>>>>>>>>>>>>>>", q_id
        que = Question.objects.get(id=q_id)
        ans = Answer.objects.filter(question=que)
        print ">>>>>>>>>>>>>>>>", que


        context = {
            'q' : que,
            'ans' : ans,
            'l' : range(1,len(ans)+1)
        }
        return render(request, 'answer_prefernce.html', context)

    def post(self, request, q_id):
        d = request.POST.items()
        for key, value in d:
            if key !='csrfmiddlewaretoken':
                mem = Answer.objects.get(id=key)
                mem.preference = value
                mem.save()
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
        soc_code = request.POST.get('soc_code')
        onet_code= request.POST.get('onet_code')
        if task_ids and task_name:
            task_obj = Aspiration.objects.create(name=task_name, onet_code=onet_code, soc_code=soc_code)
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
		'soc_code' : ob.soc_code,
		'onet_code' : ob.onet_code,
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
		'category' : ob.category,
                'type' : ob.type,
                'created_at' : ob.created_at,
                'answer_obj' : Answer.objects.filter(question=ob.id)
            }
            question_lis.append(dic_obj)
        context = {
            'question_lis' : question_lis,
        }
        return render(request, 'list_data.html', context)

class TestView(View):

    def get(self, request):

        for q in s['question']:
            a_lis = []
            print q
            asd = Question.objects.create(text=q['text'], type=q['type'], created_by=q['created_by'])
            for a in s['answer']:
                if q['id'] == a['question_id']:
                    sdsaf = Answer.objects.create(question=asd, answer=a['answer'])
                    a_lis.append(a)
            print "aaaaaaaa",a


class GetMyIp(View):

    def get(self, request):
        text = requests.get('http://ipv4.whatismyv6.com/')
        return render(request, 'ip.html', {'text' : text.content})


class SkillView(View):

    def get(self, request):
        skill_form = SkillForm()
        return render(request, 'skill.html', {'skill_form' : skill_form})

    def post(self, request):
        skill_form = SkillForm(request.POST)
        skill_form.save()
        return redirect('/skill/list')


class SkillListView(View):

    def get(self, request):
        skill_list = Skill.objects.all()
        return render(request, 'skill_list.html', {'skill_list' : skill_list})


class MapAspirationSkill(View):

    def get(self, request):
        aspiration = Aspiration.objects.all()
        skill = Skill.objects.all()
        context = {
            'aspiration' : aspiration,
            'skill' : skill
        }
        return render(request, 'aspiration_skill.html', context)

    def post(self, request):
        asp = request.POST.get('aspiration')
        skill_list = request.POST.getlist('skill')
        print 'skill_list', skill_list
        asp_obj = Aspiration.objects.get(id=asp)
        for lis in skill_list:
            s_obj = Skill.objects.get(id=lis)
            frm = AspirationSkillMapping.objects.create(aspiration=asp_obj, skill=s_obj)
        return redirect('/skill/%s/prefernce' % asp_obj.id)


class AddSkillPreferenceView(View):

    def get(self, request, pk):
        asp_obj = Aspiration.objects.get(id=pk)
        mem = AspirationSkillMapping.objects.filter(aspiration=asp_obj)
        dic_obj = {
                'id' : asp_obj.id,
                'name' : asp_obj.name,
                'skill_obj' : mem,
                'l' : range(1,len(mem)+1)
            }
        return render(request, 'skill_prefernce.html', dic_obj)

    def post(self, request, pk):
        d = request.POST.items()
        for key, value in d:
            if key !='csrfmiddlewaretoken':
                mem = AspirationSkillMapping.objects.get(id=key)
                mem.preference = value
                mem.save()
        return redirect('/skill/prefernce/list')


class SkillPrefernceList(View):

    def get(self, request):
        t = Aspiration.objects.all()
        question_lis = []
        for ob in t:
            mem = AspirationSkillMapping.objects.filter(aspiration=ob)
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
        return render(request, 'skill_prefernce_list.html', context)


class NotificationView(View):

    def get(self, request):
        not_form = NotificationForm()
        context = {
            'not_form' : not_form
        }
        return render(request, 'notification.html', context)


    def post(self, request):
        not_form = NotificationForm(request.POST)
        if not_form.is_valid():
            not_form.save()
        return redirect('/notification')










