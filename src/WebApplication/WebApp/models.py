from django.db import models
import BrowserSimulator.BrowserSimulator as BS
import SourceCodeHandler.SourceCodeHandler as SC
import Blacklist.BlacklistManager as BL
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

def validURL(url):
	if re.match(r'^https?:/{2}\w.+$', url):
		url = url.replace("https", "http", 1)
		return url
	else:
	    return ""

def urlProcess(url):
	bs = BS(url)
	sc = SC(url)
	bl = BL(url)
	Threads = []
	result = Queue()
	Threads.append(threading.Thread(target = bs.simulateManager))
	Threads.append(threading.Thread(target = sc.parse))
	Threads.append(threading.Thread(target = bl.check))
	for t in Threads:
		t.start()
	for t in Threads:
		t.join()



def __main__():
	urlProcess("127.0.0.1")

if __name__ == '__main__':
    main()	
				