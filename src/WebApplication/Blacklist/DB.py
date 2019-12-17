import WebApp.models as models

class DB():
	def check(self, url):
		try:
			data = models.BlacklistDB.objects.get(url=url)
			maliciousType = data.maliciousType
		except:
			data = models.BlacklistDB.objects.get(url=url)
			maliciousType = ""
		print(data.maliciousType)
		print(data.url)
		
		return maliciousType
	
	def update(self):
		pass
