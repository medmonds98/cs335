# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from polls.models import Poll, PollForm, Choice
from django.template import loader

def index(request):
    
    # put options in here like create new poll and vote on poll
    
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    
    t = loader.get_template('polls/index.html')
    
    c = { 'latest_poll_list': latest_poll_list, }
    
    output =', '.join([p.question for p in latest_poll_list])
    
    return HttpResponse(t.render(c))
    

def getPoll(request):
    
    #Allow the user to enter a poll
    
    if request.method =='POST': # If the form has been submitted...
        
        
        form = PollForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            # create a Choice for the given answers
            cd = form.cleaned_data
            
            c1 = Choice(poll = cd['question'], choice = cd['answer1'], votes = 0)
            c1.save()
            
            c2 = Choice(poll = cd['question'], choice = cd['answer2'], votes = 0)
            c2.save()
            
            c3 = Choice(poll = cd['question'], choice = cd['answer3'], votes = 0)
            c3.save()
            
            # return to index
            return HttpResponseRedirect('/') # Redirect after POST
            
    else:
        form = PollForm() # An unbound form
        
    return render(request, 'polls/getPoll.html', {'form': form,})
        
    
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s" % poll_id)
    
def full_results(request):
    # get full list of results
    poll_list = Poll.objects.all()
    choice_list = Choice.objects.all()
    
    t = loader.get_template('polls/fullResults.html')
    
    c = { 'poll_list':poll_list, 'choice_list': choice_list, }
    
    return HttpResponse(t.render(c))
    
def results(request, poll_id):
    poll = Poll.objects.get(id = poll_id)
    
    choice_list = []
    
    for choice in Choice.objects.all():
        if choice.poll == poll.question:
            choice_list.append(choice)
    
    t = loader.get_template('polls/results.html')
    
    c = { 'poll':poll, 'choice_list':choice_list }
    
    return HttpResponse(t.render(c))
    
@csrf_exempt
def vote(request, poll_id):
    
    # grab poll data
    poll = Poll.objects.get(id = poll_id)
    
    # create choice list
    choice_list = []
    
    for choice in Choice.objects.all():
        if choice.poll == poll.question:
            choice_list.append(choice)
    
    # set up template data
    t = loader.get_template('polls/getVote.html')
    
    c = { 'poll': poll, 'choice_list': choice_list, 'choice0': choice_list[0], 'choice1': choice_list[1], 'choice2': choice_list[2], }
    
    # let the user select a button next to their desired answer
    
    if request.method == 'POST':
            
            # grab the 'choice' value from the request
            choice_val = request.POST.get('choice')
            
            #increment the vote number here based on what choice was
            if int(choice_val) == 0:
                choice_list[0].votes += 1
                choice_list[0].save()
                
            elif int(choice_val) == 1:
                choice_list[1].votes += 1
                choice_list[1].save()
                
            elif int(choice_val) == 2:
                choice_list[2].votes += 1
                choice_list[2].save()
            
            #return to index
            return HttpResponseRedirect('/polls/' + poll_id + '/results/')
        
    else:
        form = PollForm()
    
    return HttpResponse(t.render(c))
    