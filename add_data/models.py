from __future__ import unicode_literals

from django.db import models

TYPE_CHOICE = (
    ('LONGLIST', 'LONGLIST'),
    ('TXTARR3', 'TXTARR3'),
    ('TXTMCQ2', 'TXTMCQ2'),
    ('DP', 'DP'),
    ('TC', 'TC'),
    ('LSK', 'LSK'),
    ('TXTMCQ5', 'TXTMCQ5'),
    ('TXTMCQ4', 'TXTMCQ4'),
    ('TXTMCQ3', 'TXTMCQ3'),
    ('TXT', 'TXT'),

)

class Question(models.Model):
    text = models.TextField()
    type = models.CharField(max_length=150, null=True, blank=True, choices=TYPE_CHOICE)
    created_by = models.CharField(max_length=100, null=True, blank=True, default="system")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=450)
    preference = models.CharField(max_length=90)

    class Meta:
        db_table = 'answer'


class Task(models.Model):
    name = models.CharField(max_length=120)
    question = models.ManyToManyField(Question, through='Membership')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task'


class Membership(models.Model):
    question = models.ForeignKey(Question)
    task = models.ForeignKey(Task)
    preference = models.CharField(max_length=100)


    class Meta:
        db_table = 'task_question'


class Aspiration(models.Model):
    sector = models.CharField(max_length=128)
    task = models.ManyToManyField(Task, through='TaskAspirationMapping')
    industry = models.CharField(max_length=100, null=True, blank=True)
    onet_code = models.CharField(max_length=100, null=True, blank=True)
    soc_code = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
	db_table = 'aspiration'


class TaskAspirationMapping(models.Model):
    aspiration = models.ForeignKey(Aspiration)
    task = models.ForeignKey(Task)
    preference = models.CharField(max_length=100)

    class Meta:
	db_table = 'aspiration_task'

class Skill(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'skill'


class AspirationSkillMapping(models.Model):
    aspiration = models.ForeignKey(Aspiration)
    skill = models.ForeignKey(Skill)
    preference = models.CharField(max_length=100)

    class Meta:
        db_table = 'skill_aspiration'


class Notification(models.Model):

    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    task = models.ForeignKey(Task)
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = 'notification'

