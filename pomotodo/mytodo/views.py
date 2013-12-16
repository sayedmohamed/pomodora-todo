from django.shortcuts import render
from mytodo.models import Project, Task
from django.contrib.auth.models import User
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from mytodo.forms import RegistrationForm



""" main page for the app"""

def main_page(request):
	return render(request,'mytodo/index.html',
               {'user':request.user})


def user_page(request,username):
	try:
		user=User.objects.get(username=username)
	except User.DoesNotExist:
		raise Http404('requested user does not exist')

	projects=user.project_set.all()

	return render(request,'mytodo/user_page.html',
		{'username':username,'projects':projects})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			user=User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email']
				)
			return HttpResponseRedirect('/')

	else:
		form=RegistrationForm()
	variables=RequestContext(request,{'form':form})

	return render(request,'registration/register.html',variables)