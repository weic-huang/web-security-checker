from django.shortcuts import render
from django.http import HttpResponse
import re
from WebApp.models import Model



class Frontend():
	
	def __init__(self):
		self.url_mode = 0
		self.url_alert = 0
		self.model=Model()
		print("init test")

	def index(self,request):

		enterurl = request.POST.get('URL_input') 
		if enterurl!=None: # type url 
			print("change to back");
			print("mode: ",self.url_mode );
			print("alert: ",self.url_alert );
			url = "" #self.model.validURL(enterurl);
			if url=="": #get wrong url
				self.url_mode = 0
				self.url_alert = 1
			else : #get correct url
				self.url_mode = 1
				self.url_alert = 0
			print(self.url_mode );
			print(self.url_alert );
		

		if self.url_mode==1:
			return render(request, './indexpage.html',{'url_alert':self.url_alert,'url_output':enterurl})
		else:
			print("url_mode=1")
			Result=self.model.urlProcess(url)
			return render(request, './resultpage.html',{
					'url':url,
					'BlacklistResult':Result.BlackListManager,
					'BrowserSimulatorResult':Result.BrowserSimulator,
					'SourceCodeHandler':Result.SourceCodeHandler,
					})

		
	

