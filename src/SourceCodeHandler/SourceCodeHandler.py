# need to add some import files
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
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

		options = Options()
		# not to show the window
		options.add_argument("--headless")
		# not to print console message in cmd
		options.add_argument('log-level=1')

		driver = webdriver.Chrome(chrome_options=options,executable_path="./include/chromedriver.exe")
		driver.get(self.url)

		soup = BeautifulSoup(driver.page_source, "html.parser")
		scripts = soup.find_all('script')
		srcs = [i.get('src') for i in scripts if i.get('src')]

		# get all src path from other website
		for s in srcs:
			if s[0:4] == "http":
				self.srcPaths.append(s)


		self.sourceCode = driver.page_source
		a = [m.start() for m in re.finditer('function', self.sourceCode)]

		# get all js functions
		for i in a:
			now = i
			flag = 0
			while flag == 0:
				if self.sourceCode[now] == "{":
					flag += 1
				now += 1

			while flag > 0:
				if self.sourceCode[now] == "{":
					flag += 1
				if self.sourceCode[now] == "}":
					flag -= 1
				now += 1

			self.JSfunctions.append(self.sourceCode[i:now])




	def callMiningChecker(self):
		# as title
		pass

	def callJSScanner(self):
		# as title
		pass

	def callHtmlScanner(self):
		# as title
		pass
