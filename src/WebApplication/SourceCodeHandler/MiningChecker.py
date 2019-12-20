# Should import db files
import WebApp.models as models

class MiningChecker():
	
	def __init__(self, JSfunctions, srcPaths):
		self.JSfunctions = JSfunctions
		self.srcPaths = srcPaths

	def call(self):
		outputValue = {"isMining": False,
						"miningType": ""}

		DBresult = self.checkBlocklistFromDB()
		print(DBresult)
		outputValue["isMining"] = DBresult["isMining"]
		outputValue["miningType"] = DBresult["miningType"]

		scriptResult = self.checkMiningScript()
		outputValue["isMining"] = scriptResult | outputValue["isMining"]

				
		return outputValue


	def checkBlocklistFromDB(self):
		
		output = {"isMining" : False,
			"miningType" : "Unrecognized"}
		for path in self.srcPaths:
			data = models.MininglistDB.objects.filter(url=path)
			if data:				
				return {"isMining" : True,
						"miningType" : "Unrecognized"}
		return output

		

	def checkMiningScript(self):
		# as title
		return False


