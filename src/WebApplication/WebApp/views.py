from django.shortcuts import render
from django.http import HttpResponse
import re
from WebApp.models import Model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
	
	
class Frontend():
	def __init__(self):
		self.model=Model("")
		self.url=""
		print("init Frontend")

	def index(self,request):
		url_mode = 0
		url_alert = 0
		enterurl = request.POST.get('URL_input',None)
		self.model.renewModel("")

		if enterurl!=None: # type url 

			self.url = enterurl
			self.model.url=enterurl
			url = self.model.validURL();
			
			if url=="": #get wrong url
				url_mode = 0
				url_alert = 1
			else : #get correct url
				url_mode = 1
				url_alert = 0
		else:
			url_alert=0


		if url_mode==0:
			return render(request, './indexpage.html',{'url_alert':url_alert,'url_output':enterurl})
		else :
			
			return render(request, './resultpage.html',{
					'url':url,
					})

	def startprocess(self,request):
		self.model.urlProcess(self.url);
		print("end process")
		return JsonResponse({"test":"test"})

	def ajax_SC(self,request):
		#print("start SC")
		while True:
			SC_Result=self.model.get_result("SC")
			if (SC_Result!=None):
				break
			time.sleep(1)
		return_dict= {
		'isMining': "{}".format(SC_Result.isMining),
		'miningType': SC_Result.miningType,
		'hasAutoDownload' : "{}".format(SC_Result.hasAutoDownload),
		'hasPopUp' : "{}".format(SC_Result.hasPopUp),
		'hasHiddenObject' : "{}".format(SC_Result.hasHiddenObject),
		'hasNotification' : "{}".format(SC_Result.hasNotification),
		'hasHardwareAccess' : SC_Result.hasHardwareAccess
		}
		#print("end SC")
		return JsonResponse(return_dict)


	def ajax_BL(self,request):
		#print("start BL")
		while True:
			BL_Result=self.model.get_result("BL")
			if (BL_Result!=None):
				break
			time.sleep(1)

		return_dict= {
		'maliciousType': BL_Result.maliciousType,
		}
		#print("end BL")
		return JsonResponse(return_dict)

	def ajax_BS(self,request):
		#print("start BS")
		while True:
			BS_Result=self.model.get_result("BS")
			if (BS_Result!=None):
				break
			time.sleep(1)
		return_dict= {
		'mem': BS_Result.usage.mem,
		'cpu': BS_Result.usage.cpu,
		'viewfilename' : BS_Result.viewfilename
		}
		#print("end BS")
		return JsonResponse(return_dict)



		
