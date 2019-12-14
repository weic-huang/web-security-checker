from Blacklist import BlacklistResult
from BrowserSimulator import BrowserSimulatorResult
from SourceCodeHandler import SourceCodeHandlerResult

class Result():
	def __init__(self, url):
		self.Url = url
		self.BlackListManager = BlacklistResult()
		self.BrowserSimulator = BrowserSimulatorResult()
		self.SourceCodeHandler = SourceCodeHandlerResult()