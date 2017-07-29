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
	type = models.CharField(max_length=100, null=True, blank=True, choices=TYPE_CHOICE)
	created_by = models.CharField(max_length=100, null=True, blank=True, default="system")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

	class Meta:
		db_table = 'question'


class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer = models.CharField(max_length=400)

	class Meta:
		db_table = 'answer'


class Task(models.Model):
    name = models.CharField(max_length=128)
    question = models.ManyToManyField(Question, through='Membership')

    class Meta:
		db_table = 'task'


class Membership(models.Model):
    question = models.ForeignKey(Question)
    task = models.ForeignKey(Task)
    preference = models.CharField(max_length=100)


    class Meta:
		db_table = 'task_question'