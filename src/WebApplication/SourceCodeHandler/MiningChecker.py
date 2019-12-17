# Should import db files
import WebApp.models as models

class MiningChecker():
	
	def __init__(self, JSfunctions, srcPaths):
		self.JSfunctions = JSfunctions
		self.srcPaths = srcPaths

	def call():
		outputValue = {"isMining": False,
						"miningType": ""}

		DBresult = self.checkBlocklistFromDB()
		outputValue["isMining"] = DBresult["isMining"]
		outputValue["miningType"] = DBresult["miningType"]

		scriptResult = self.checkMiningScript()
		outputValue["isMining"] = scriptResult

				
		return outputValue


	def checkBlocklistFromDB(self):
		
		for path in self.srcPaths:
			try:
				data = models.MininglistDB.objects.get(url=url)
				if data != None:
					return {"isMining" : True,
							"miningType" : "Unrecognized"}
			except:
				continue

		

	def checkMiningScript(self):
		# as title
		return False


