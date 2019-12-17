

class BlacklistResult():
	def __init__(self, maliciousType):
		self.maliciousType = maliciousType
	
	def getResult(self):
		return self.maliciousType
		