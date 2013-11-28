from django.shortcuts import render
from django.views.generic import ListView
from mytodo.models import Project


class ListProjectView(ListView):
	model=Project
