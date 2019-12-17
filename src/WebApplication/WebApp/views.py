from django.shortcuts import render
from django.http import HttpResponse
import re
from WebApp.models import Model



def index(request):
	url_mode = 0
	url_alert = 0
	enterurl = request.POST.get('URL_input') 
	url=""
	if enterurl!=None:
		url = Model.validURL(enterurl);
		if url=="":
			url_mode = 0
			url_alert = 1
		else :
			url_mode = 1
			Result=Model.urlProcess(url)



	if url_mode==0:
		return render(request, './indexpage.html',{'url_alert':url_alert,'url_output':enterurl})
	else:
		return render(request, './resultpage.html',{
		'url':url,
		'BlacklistResult':Result.BlackListManager,
		'BrowserSimulatorResult':Result.BrowserSimulator,
		'SourceCodeHandler':Result.SourceCodeHandler,
		'item' : ["isMining","MiningType","isAutoDownload","hasPopUp","hasHiddenObject","hasNotification","hasHardwareAccess"]
		})#result



