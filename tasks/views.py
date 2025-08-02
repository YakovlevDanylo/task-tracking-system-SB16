from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
