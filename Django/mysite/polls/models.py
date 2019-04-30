# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, Textarea, Form, RadioSelect

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    answer1 = models.CharField(max_length = 200)
    answer2 = models.CharField(max_length = 200)
    answer3 = models.CharField(max_length = 200)
    
class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'pub_date', 'answer1', 'answer2', 'answer3',]
        widgets = {
            'title' : Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    
class Choice(models.Model):
    poll = models.CharField(max_length = 200)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
