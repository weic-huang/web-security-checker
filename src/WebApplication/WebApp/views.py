from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	url_success = 0


	if url_success==0:
		return render(request, './indexpage.html',{'url_success':url_success})
	else:
		return render(request, './resultpage.html',{
		'url':"",
		'BlacklistResult':"",
		'BrowserSimulatorResult':{"MEM":"","CPU":"","IMG":""},
		'SourceCodeHandler':""})#result