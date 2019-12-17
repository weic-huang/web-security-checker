from Blacklist.Cache import Cache
from Blacklist.DB import DB
from Blacklist.ThirdParty import ThirdParty

class BlacklistManager():
	def __init__(self, url):
		self.url = url

	def check(self):

		result = self.checkCache()
		if result != "":
			return result

		#result = self.checkDB()
		if result == "":
			result = self.checkThirdParty()

		if result == "":
			result = "safe URL"

		self.updateCache(result)

		return BlacklistResult(result)

	def checkCache(self):
		cache = Cache()

		return cache.check(self.url)

	def updateCache(self, blacklistResult):
		cache = Cache()		
		cache.update(self.url, blacklistResult)
		return

	def checkDB(self):
		db = DB()

		return db.check(self.url)

	def checkThirdParty(self):
		APIKEY = ""
		thirdParty = ThirdParty(APIKEY)

		return thirdParty.check(self.url)

class BlacklistResult():
	def __init__(self, maliciousType):
		self.maliciousType = maliciousType
