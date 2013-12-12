from django.shortcuts import render
from mytodo.models import Project, Task


""" main page for the app"""


def main_page(request):
    return render(request,'mytodo/index.html')