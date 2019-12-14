from django.shortcuts import render
from django.http import HttpResponse
import re
def index(request):
	url_mode = 0
	url_alert = 0
	enterurl = request.POST.get('URL_input') 
	url=""
	if enterurl!=None:
		url = validURL(enterurl);
		if url=="":
			url_mode = 0
			url_alert = 1
		else :
			url_mode = 1

	if url_mode==0:
		return render(request, './indexpage.html',{'url_alert':url_alert,'url_output':enterurl})
	else:
		return render(request, './resultpage.html',{
		'url':url,
		'BlacklistResult':"",
		'BrowserSimulatorResult':{"MEM":0.0,"CPU":0.0,"IMG":"img_filename"},
		'SourceCodeHandler':{'isMining':"true",'mining_type':"string",'isAutoDownload':"true",
					'hasPoPUp':"true",'hasHiddenObject':"true",'hasNotification':"true",'hasHardwareAccess':"string"}

		})#result


def validURL(url):
	if re.match(r'^https?:/{2}\w.+$', url):
		url = url.replace("https", "http", 1)
		return url
	else:
	    return ""
