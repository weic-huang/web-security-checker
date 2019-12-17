from Blacklist.BlacklistManager import BlacklistResult
from BrowserSimulator.BrowserSimulator import BrowserSimulatorResult
from SourceCodeHandler.SourceCodeHandlerResult import SourceCodeHandlerResult

class Result():
	def __init__(self, url):
		self.Url = url
		self.BlackListManager = None
		self.BrowserSimulator = None
		self.SourceCodeHandler = None
