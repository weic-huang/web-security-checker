# need to add some import files
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SourceCodeHandler.HtmlScanner import HtmlScanner
from SourceCodeHandler.JSScanner import JSScanner
from SourceCodeHandler.MiningChecker import MiningChecker
from SourceCodeHandler.SourceCodeHandlerResult import SourceCodeHandlerResult

from urllib.parse import urlparse
import re
import validators
import time

# Instructions:
# Just new a SourceCodeHandler() object with url
# then call call(), it will return what you want

class SourceCodeHandler():

	def __init__(self,url):
		self.url = url
		self.sourceCode = ""
		self.HtmlObject = []
		self.JSfunctions = []
		self.srcPaths = []

	def call(self):
		self.sourceCode = ""
		self.HtmlObject = []
		self.JSfunctions = []
		self.srcPaths = []
		outputData = {}
		outputData = {**outputData, **self.callHtmlScanner()}
		outputData = {**outputData, **self.callJSScanner()}
		outputData = {**outputData, **self.callMiningChecker()}
		output = SourceCodeHandlerResult(outputData)
		return output


	def parse(self):
		# use self.url to build other attribute

		options = Options()
		# not to show the window
		options.add_argument("--headless")
		# not to print console message in cmd
		options.add_argument('log-level=1')
		driver = webdriver.Chrome(chrome_options=options,executable_path="../../include/chromedriver.exe")

		try:
			driver.get(self.url)
			soup = BeautifulSoup(driver.page_source, "html.parser")
			scripts = soup.find_all('script')
			eles = driver.find_elements_by_xpath('//*')

		except:
			scripts = []
			eles = []
		
		srcs = [i.get('src') for i in scripts if i.get('src')]
		srcs.append(self.url)

		#######################################
		# Get all src path from other website #
		#######################################
		for s in srcs:
			o = urlparse(s)
			if s[0:4] == "http":
				self.srcPaths.append(o.netloc)
		print("src paths Done")


		self.sourceCode = driver.page_source
		a = [m.start() for m in re.finditer('function', self.sourceCode)]

		#####################################
		#		get all js functions		#
		#####################################
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
		print("src js functions Done")

		#####################################
		#		get all Html Objects		#
		# 			with visibility			#
		#####################################
		allElements = []
		
		for ele in eles:
			try:
				ss = ele.get_attribute("outerHTML")	
			except:
				continue
			# ss = "<>"

			if ss[0] != "<":
				# TODO
				# Here should be some log message!!
				continue

			else:
				i = 1
				flag = 1
				isvisible = ""
				while flag != 0:
					if ss[i] == "<":
						flag += 1
					if ss[i] == ">":
						flag -= 1
					i += 1
				# This function can extend the hidden css of elements
				isvisible = ele.value_of_css_property("visibility")
				v = " visibility:" + isvisible


				ss = ss[0:i-1] + v + ">"				
				allElements.append(ss)

		self.HtmlObject = allElements

		print("src HtmlObject Done")


	def callMiningChecker(self):
		MinigObj = MiningChecker(self.JSfunctions, self.srcPaths)
		result = MinigObj.call()
		return result


	def callJSScanner(self):
		JSObj = JSScanner()
		result = JSObj.checkMaliciousBehavior(self.JSfunctions)
		return result

	def callHtmlScanner(self):
		HtmlObj = HtmlScanner()
		if len(self.HtmlObject) == 0:
			result = False
		else:
			result = HtmlObj.checkHiddenObject(self.HtmlObject)
		return {"hasHiddenObject" : result}