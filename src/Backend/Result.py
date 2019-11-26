from BlackList import BlackListManager
from BrowserSimulator import BrowserSimulator
from SourceCodeHandler import SourceCodeHandler

class Result():
	def __init__(self, url):
		self.Url = url
		self.BlackListManager = BlackListManager()
		self.BrowserSimulator = BrowserSimulator()
		self.SourceCodeHandler = SourceCodeHandler()