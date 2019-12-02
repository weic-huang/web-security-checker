import requests

class ThirdParty():
	def __init__(self,APIKEY):
		self.APIKEY = APIKEY

	def check(self, url):
		# malicious url
		# "http://13453765871837679316.googlegroups.com/attach/5ed5d019a6363180/docfile.htm?part=0.1&view=1&vt=ANaJVrEeittmQwMxZJXRcDdPNLE2-gXGwGja7dnY6uPBYHXdeIAepWdlcx0i0SZ1YQhTDOduB7hNyqrKz6SyrwDQWlgfISVaRZcF3L5QvzKOv-oZ09G491A"

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

		result = requests.post(url = URL, json = DATA, params = PARA).json()

		threatType = ""
		if result:
			threatType = result['matches'][0]['threatType']

		return threatType

	def updateKey(self):
		pass
