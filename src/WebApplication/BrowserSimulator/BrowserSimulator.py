from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import subprocess
import psutil
import sys
import time

class BrowserSimulator():
	def __init__(self, url):
		self.url = url
		self.simulateManager()
	
	def simulateManager(self):
		self.simulator()
	
	def simulator(self):
		self.proc = subprocess.Popen(['python3', 'simulate.py', self.url],
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT)
		time.sleep(0.1)
		self.getUsage()
		self.proc.stdout.readline()
		self.proc.terminate()
		try:
			self.proc.wait(timeout=0.2)
			print('exit with rc = ', self.proc.returncode)
		except subprocess.TimeoutExpired:
			print('not terminate in time')

	
	def getUsage(self):
		infoUsage = psutil.Process(self.proc.pid)
		mem = infoUsage.memory_info().rss / 1024 #kb
		cpu = infoUsage.cpu_percent(interval=0.1)
		print (mem)
		print (cpu)
		self.result = UsageData(mem, cpu)
	
	def getView(self):
		pass

class UsageData():
	def __init__(self, mem, cpu):
		self.mem = mem
		self.cpu = cpu

# BrowserSimulator('test')
