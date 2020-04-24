from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,Http404
from  django.template import  RequestContext
from  django.contrib.auth.models import  User
from django.db import  models
from .models import List

# Create your views here.
#
# def todo_list(request):
#
#     todolist = List.objects.all()
#
#     return  render_to_response('status_report.html',{'todolist':todolist})
#
def status_report(request):

  todo_listing = []
  
   # 返回所有列表

  
  for todo_list in List.objects.all():
    
    todo_dict = {}

    todo_dict['list_object'] = todo_list

    todo_dict['item_count'] = todo_list.item_set.count()

    todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()

    todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)

    todo_listing.append(todo_dict)
  # todo_list = List.objects.all()

  return render_to_response('status_report.html', { 'todo_listing': todo_listing })