from Blacklist import BlacklistResult
from BrowserSimulator import BrowserSimulatorResult
from SourceCodeHandler import SourceCodeHandlerResult

class Result():
	def __init__(self, url):
		self.Url = url
		self.BlackListManager = BlacklistResult.BlacklistResult()
		self.BrowserSimulator = BrowserSimulatorResult.BrowserSimulatorResult()
		self.SourceCodeHandler = SourceCodeHandlerResult.SourceCodeHandlerResult()