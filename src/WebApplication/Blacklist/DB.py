import WebApp.models as models

class DB():
	def check(self, url):
		try:
			data = models.BlacklistDB.objects.get(url=url)
			maliciousType = data.maliciousType
		except:
			maliciousType = ""
		print(maliciousType)
		
		return maliciousType
	
	def update(self):
		pass
