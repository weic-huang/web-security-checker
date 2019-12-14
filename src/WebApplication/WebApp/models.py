from django.db import models
import BrowserSimulator.BrowserSimulator as BS
import SourceCodeHandler.SourceCodeHandler as SC
import Blacklist.BlacklistManager as BL
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
	def validURL(url):
		if re.match(r'^https?:/{2}\w.+$', url):
			url = url.replace("https", "http", 1)
			return url
		else:
		    return ""

	def urlProcess(url):
		print("hi")
		bs = BS.BrowserSimulator(url)
		sc = SC.SourceCodeHandler(url)
		bl = BL.BlacklistManager(url)
		"""bsResult = MyThread(target = bs.simulateManager)
		scResult = MyThread(target = sc.parse)
		blResult = MyThread(target = bl.check)
		bsResult.start()
		scResult.start()
		blResult.start()
		print(bsResult.get_result())
		print(scResult.get_result())
		print(blResult.get_result())"""
		return Result(url)




def __main__():
	urlProcess("127.0.0.1")

if __name__ == '__main__':
    main()	
				