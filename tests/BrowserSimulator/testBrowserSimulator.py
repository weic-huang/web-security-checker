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

		self.assertIsInstance(self.s.usage, UsageData)
		self.assertIsInstance(self.s.usage.mem, (float,int))
		self.assertIsInstance(self.s.usage.cpu, (float,int))


	def testSimulateManager(self):
		BrowserSimulator.simulator = mockSimulator
		self.s.simulateManager()

		self.assertIsInstance(self.s.result, BrowserSimulatorResult)
		self.assertIsInstance(self.s.result.viewfilename, str)
		self.assertEqual(self.s.result.viewfilename[-4:], ".png")