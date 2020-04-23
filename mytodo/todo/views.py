from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,Http404
from  django.template import  RequestContext
from  django.contrib.auth.models import  User
from .models import todo

# Create your views here.

def todo_list(request):
    
    todolist = todo.objects.all()
    
    return  render_to_response('todo.html',{'todolist':todolist})
    
