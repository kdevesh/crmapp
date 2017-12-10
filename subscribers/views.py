from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SubscriberForm

# Create your views here.

def subscriber_new(request):
	if request.method=='POST':
		form=SubscriberForm(request.POST)
		if(form.is_valid()):
			username=form.cleaned_data.get('username')
			email=form.cleaned_data.get('email')
			password=form.cleaned_data.get('password1')
			user=User(username=username,email=email)
			user.set_password(password)
			user.save()
			return HttpResponseRedirect('/success/')
		else:
			form=SubscriberForm()
	return render(request, 'subscribers/subscriber_new.html', {'form':form})