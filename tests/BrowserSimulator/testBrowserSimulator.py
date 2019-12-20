import unittest
import os
from src.WebApplication.BrowserSimulator.BrowserSimulator import BrowserSimulator
from src.WebApplication.BrowserSimulator.BrowserSimulator import UsageData
from src.WebApplication.BrowserSimulator.BrowserSimulator import BrowserSimulatorResult

class mockProcess(object):
	pid = os.getpid()

def mockSimulator(self):
	self.proc = mockProcess()
	self.getUsage()

class BrowserSimulatorTest(unittest.TestCase):

	def setUp(self):
		self.s = BrowserSimulator("http://www.example")

	def testGetUsage(self):
		self.s.proc = mockProcess()

		self.s.getUsage()
		print(self.s.usagedata.cpu)

		self.assertIsInstance(self.s.usagedata, UsageData)
		self.assertIsInstance(self.s.usagedata.mem, (float,int))
		self.assertIsInstance(self.s.usagedata.cpu, (float,int))


	def testSimulateManager(self):
		BrowserSimulator.simulator = mockSimulator
		self.s.simulateManager()

		self.assertIsInstance(self.s.result, BrowserSimulatorResult)
		self.assertIsInstance(self.s.result.viewfilename, str)
		self.assertEqual(self.s.result.viewfilename[-4:], ".png")