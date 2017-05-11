# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect , Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    entries =  Entry.objects.all().order_by('-date_added')
    context = {'entries': entries}
    return render(request,"LearningLogs/index.html", context)

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics':topics}
    return render(request,'LearningLogs/topics.html',context)


@login_required
def topic(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'LearningLogs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return HttpResponseRedirect(reverse("LearningLogs:topics"))
    context = {'form':form}
    return render(request,'LearningLogs/new_topic.html',context)


@login_required
def new_entry(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    check_topic_owner(request, topic)


    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return HttpResponseRedirect(reverse('LearningLogs:topic',
                                                args=[topic.slug]))

    context = {'topic': topic, 'form': form}
    return render(request, 'LearningLogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    public = entry.public
    if request.method != "POST":
        form = EntryForm(instance=entry, initial={"public" : public})
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            edit_entry = form.save(commit=False)
            if request.POST.get("public"):
               edit_entry.public = True
            else:
                edit_entry.public = False
            edit_entry.save()
            return HttpResponseRedirect(reverse('LearningLogs:topic', args=[topic.slug]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'LearningLogs/edit_entry.html',context)

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404


