from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from tasks.models import Task
from tasks.forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task-list")