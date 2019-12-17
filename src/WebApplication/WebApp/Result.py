from Blacklist.BlacklistResult import BlacklistResult
from BrowserSimulator.BrowserSimulator import SimulatorResult
from SourceCodeHandler.SourceCodeHandlerResult import SourceCodeHandlerResult

class Result():
	def __init__(self, url):
		self.Url = url
		self.BlackListManager = BlacklistResult("")
		self.BrowserSimulator = SimulatorResult()
		self.SourceCodeHandler = SourceCodeHandlerResult()