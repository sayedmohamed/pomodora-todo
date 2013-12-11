from django.shortcuts import render
from django.views.generic import ListView
from mytodo.models import Project,Task


""" index page ,listing user lists or projects"""
class ListProjectView(ListView):
	model=Project


""" list project related task """
class ListTaskView(ListView):
	model=Task
