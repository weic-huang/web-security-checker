from django.shortcuts import render
from django.http import HttpResponse
import re
from WebApp.models import Model

class Frontend():
	
	def __init__(self):
		self.url_mode = 0
		self.url_alert = 0
		self.model=Model("")
		self.url=""
		

	def index(self,request):
		self.url_mode = 0
		enterurl = request.POST.get('URL_input') 
		if enterurl!=None: # type url 
			
			self.model.url=enterurl
			url = self.model.validURL();
			
			if url=="": #get wrong url
				self.url_mode = 0
				self.url_alert = 1
				self.url=""
			else : #get correct url
				self.url_mode = 1
				self.url_alert = 0
				self.url=enterurl
		else:
			self.url_alert=0


		if self.url_mode==0:
			return render(request, './indexpage.html',{'url_alert':self.url_alert,'url_output':enterurl})
		else :
			Result=self.model.get_result()
			return render(request, './resultpage.html',{
					'url':self.url,
					'BlacklistResult':Result.BlackListManager,
					'BrowserSimulatorResult':Result.BrowserSimulator,
					'SourceCodeHandler':Result.SourceCodeHandler,
					})

		
