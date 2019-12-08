# need to add some import files
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import validators


class SourceCodeHandler():
	def __init__(self,url):
		self.url = url
		self.sourceCode = ""
		self.HtmlObject = {}
		self.JSfunctions = []
		self.srcPaths = []

	def parse(self):
		# use self.url to build other attribute
		options = Options();
		options.add_argument("--headless");

		driver = webdriver.Chrome(chrome_options=options,executable_path="./include/chromedriver.exe");
		driver.get(self.url)

		soup = BeautifulSoup(driver.page_source, "html.parser")
		srcs = [i.get('src') for i in soup.find_all('script') if i.get('src')]



	def callMiningChecker(self):
		# as title
		pass

	def callJSScanner(self):
		# as title
		pass

	def callHtmlScanner(self):
		# as title
		pass
