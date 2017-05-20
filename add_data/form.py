import re
from django import forms
from django.forms import ModelForm
from .models import Question, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['created_by', 'created_at']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : "form-control"})
        self.fields['type'].widget.attrs.update({'class' : "form-control"})
        self.fields['text'].widget.attrs['rows'] = 4
        self.fields['text'].widget.attrs['columns'] = 15

class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class' : "form-control"})
        self.fields['answer'].widget.attrs.update({'class' : "form-control"})

