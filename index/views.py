from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from .forms import *
from django.contrib import messages


def myindex(request):
	qs1 = post.objects.filter(category='C')
	qs2 = post.objects.filter(category='H')
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will reply you shortly')
			return redirect('indexurl:index')
	else:
		form = Contactform()
	context={'data':qs1,'help':qs2}
  
	return render(request, 'index/index.html', context)

def donation(request):
	if request.method == 'POST':
		form = donationform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your request  we will reply you shortly on your email!.....')
			return redirect('indexurl:donation')
	else:
		form = donationform()
	return render(request, 'index/donation.html')

# Create your views here.
