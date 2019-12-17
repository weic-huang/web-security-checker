from django.core.cache import cache

class Cache():	
	def check(self, url):
		return cache.get(url, "")
	
	def update(self, url, maliciousType):
		cache.set(url, maliciousType, 30)
		
