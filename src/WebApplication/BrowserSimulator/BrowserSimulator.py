from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import subprocess
import psutil
import sys
import time
import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


class BrowserSimulator():
	def __init__(self, url):
		self.url = url
		self.simulateManager()
	
	def simulateManager(self):
		self.viewfilename = randomString(10)
		self.simulator()
		self.result = SimulatorResult(self.usagedata, self.viewfilename)
		# print(self.result.usagedata.mem)
		# print(self.result.usagedata.cpu)
		# print(self.result.viewfilename)
	
	def simulator(self):
		self.proc = subprocess.Popen(
			['python3', 'simulate.py', self.url, self.viewfilename],
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT)
		time.sleep(0.3)
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
		self.usagedata = UsageData(mem, cpu)
	
	def getView(self):
		pass

class UsageData():
	def __init__(self, mem, cpu):
		self.mem = mem
		self.cpu = cpu

class SimulatorResult():
	def __init__(self, usagedata, viewfilename):
		self.usagedata = usagedata
		self.viewfilename = viewfilename

# BrowserSimulator('test')
