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
	
	def simulateManager(self):
		self.viewfilename = randomString(10) + ".png"
		self.simulator()
		self.result = SimulatorResult(self.usagedata, self.viewfilename)
		return self.result
	
	def simulator(self):
		self.proc = subprocess.Popen(
			['python3', 'BrowserSimulator/Simulate.py', self.url, self.viewfilename],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT)
		msg = self.proc.stdout.readline()
		self.getUsage()
		self.proc.stdin.write(b"done\n")
		self.proc.stdin.flush()
		try:
			self.proc.wait()
			# print('exit with rc = ', self.proc.returncode)
		except subprocess.TimeoutExpired:
			print('not terminate in time')

	
	def getUsage(self):
		infoUsage = psutil.Process(self.proc.pid)
		mem = infoUsage.memory_info().rss / 1024 #kb
		cpu = infoUsage.cpu_percent(interval=0.1)
		cpu = 0
		self.usagedata = UsageData(mem, cpu)

class UsageData():
	def __init__(self, mem, cpu):
		self.mem = mem
		self.cpu = cpu

class SimulatorResult():
	def __init__(self, usagedata, viewfilename):
		self.usagedata = usagedata
		self.viewfilename = viewfilename

if __name__ == "__main__":
	s = BrowserSimulator("https://www.mobile01.com/topicdetail.php?f=37&t=5886669")
	s.simulateManager()
	result = s.getResult()
	print(result.viewfilename)
	print(result.usagedata.mem)
	print(result.usagedata.cpu)
