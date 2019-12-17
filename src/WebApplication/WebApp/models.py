from django.db import models
from BrowserSimulator.BrowserSimulator import BrowserSimulator
from SourceCodeHandler.SourceCodeHandler import SourceCodeHandler
from Blacklist.BlacklistManager import BlacklistManager
from WebApp.Result import Result
from queue import Queue
import threading
import sys
import re

# Create your models here.
class BlacklistDB(models.Model):

    # Fields
	url = models.TextField(help_text='url')
	maliciousType = models.CharField(max_length=255, help_text='Malicious information of the url')

    # Methods
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of MyModelName."""
		return reverse('blacklistURL-detail', args=[str(self.id)])
    
	def __str__(self):
		"""String for representing the MyModelName object (in Admin site etc.)."""
		return self.url


class MininglistDB(models.Model):

    # Fields
	url = models.TextField(help_text='url')
	WebsiteName = models.TextField(help_text='website name of the url')

    # Methods
	def get_absolute_url(self):
		return reverse('mininglistURL-detail', args=[str(self.id)])
    
	def __str__(self):
		return self.url	

class MyThread(threading.Thread):
    def __init__(self, target=None, args=(), **kwargs):
        super(MyThread, self).__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if self.target == None:
            return
        self.result = self.target(*self.args, **self.kwargs)

    def get_result(self):
        self.join()#當需要取得結果值的時候阻塞等待子執行緒完成
        return self.result

class Model(object):
	def __init__(self, url):
		self.url = url
		self.result = Result(url)
	def validURL(self):
		if re.match(r'^https?:/{2}\w.+$', self.url):
			self.url = self.url.replace("https", "http", 1)
			return self.url
		else:
		    return ""

	def urlProcess(self, url):
		
		bs = BrowserSimulator(url)
		sc = SourceCodeHandler(url)
		bl = BlacklistManager(url)
		bsResult = MyThread(target = bs.simulateManager)
		scResult = MyThread(target = sc.call)
		blResult = MyThread(target = bl.check)
		bsResult.start()
		scResult.run()
		blResult.start()
		#print(bsResult.get_result())
		#print(scResult.get_result())
		self.result.SourceCodeHandler = scResult.get_result()
		self.result.BrowserSimulator = bsResult.get_result()
		self.result.BlacklistManager = blResult.get_result()
		print(self.result.SourceCodeHandler.isMining)
		print(self.result.SourceCodeHandler.miningType)
		print(self.result.SourceCodeHandler.hasAutoDownLoad)
		print(self.result.SourceCodeHandler.hasPipUp)
		return self.result
	def get_result(self, url):
		return self.result




def __main__():
	urlProcess("127.0.0.1")

if __name__ == '__main__':
    main()	
				