import requests

class ThirdParty():
	def __init__(self,APIKEY):
		self.APIKEY = APIKEY

	def check(self, url):
		URL, PARA, DATA = self.setRequest(url)

		threatType = ""
		try:
			r = requests.post(url = URL, json = DATA, params = PARA, timeout = 3)
			r.raise_for_status()
			result = r.json()
			if 'matches' in result:
				threatType = result['matches'][0]['threatType']

			print("third party request success")

		except requests.exceptions.Timeout as errt:
			print ("Timeout Error:", errt)

		except requests.exceptions.HTTPError as errh:
			print ("Http Error:", errh)

		except requests.exceptions.ConnectionError as errc:
			print ("Error Connecting:", errc)

		except requests.exceptions.RequestException as err:
			print ("Error:", err)

		return threatType

	def setRequest(self, url):
		URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find?"
		PARA = {'key': self.APIKEY}
		DATA = {
			"client": {
				"clientId":      "websecuritybrowser",
				"clientVersion": "1.5.2"
			},
			"threatInfo": {
				"threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
				"platformTypes":    ["ALL_PLATFORMS"],
				"threatEntryTypes": ["URL"],
				"threatEntries": [
					{"url": url},
				]
			}
		}

		return URL, PARA, DATA

	def updateKey(self):
		pass
