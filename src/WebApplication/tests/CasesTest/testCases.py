from django.test import TestCase
from WebApp.models import Model

class CasesTest(TestCase):

	def testRC1_1(self):
		# Scenario 1-1 - Successful enter a URL and get result
		# Return valid result (no suspicious condition)
		M = Model("http://sample.com")
		r = M.urlProcess("http://sample.com")

		self.assertEqual(r.BlacklistManager.maliciousType, 'safe URL')

		self.assertEqual(r.SourceCodeHandler.isMining, False)
		self.assertEqual(r.SourceCodeHandler.miningType, 'Unrecognized')
		self.assertEqual(r.SourceCodeHandler.hasAutoDownload, False)
		self.assertEqual(r.SourceCodeHandler.hasPopUp, False)
		self.assertEqual(r.SourceCodeHandler.hasHiddenObject, False)
		self.assertEqual(r.SourceCodeHandler.hasNotification, False)
		self.assertEqual(r.SourceCodeHandler.hasHardwareAccess, {})

		self.assertLessEqual(r.BrowserSimulator.usage.mem, 2000)
		self.assertNotEqual(r.BrowserSimulator.viewfilename, "")

	def testRC1_4(self):
		# Scenario 1-4 - Successful enter a URL that accesses hardware and get result
		# Return valid result (find hardware access)
		M = Model("https://davidwalsh.name/demo/camera.php")
		r = M.urlProcess("https://davidwalsh.name/demo/camera.php")

		self.assertEqual(r.BlacklistManager.maliciousType, 'safe URL')

		self.assertEqual(r.SourceCodeHandler.isMining, False)
		self.assertEqual(r.SourceCodeHandler.miningType, 'Unrecognized')
		self.assertEqual(r.SourceCodeHandler.hasAutoDownload, False)
		self.assertEqual(r.SourceCodeHandler.hasPopUp, False)
		self.assertEqual(r.SourceCodeHandler.hasHiddenObject, False)
		self.assertEqual(r.SourceCodeHandler.hasNotification, False)
		self.assertNotEqual(r.SourceCodeHandler.hasHardwareAccess, {})

		self.assertLessEqual(r.BrowserSimulator.usage.mem, 2000)
		self.assertNotEqual(r.BrowserSimulator.viewfilename, "")

	def testRC1_5(self):
		# Scenario 1-5 - Successful enter a URL that has notification access and get result
		# Return valid result (find notification access)
		M = Model("https://kkplay3c.net/141126-2/")
		r = M.urlProcess("https://kkplay3c.net/141126-2/")

		self.assertEqual(r.BlacklistManager.maliciousType, 'safe URL')

		self.assertEqual(r.SourceCodeHandler.isMining, False)
		self.assertEqual(r.SourceCodeHandler.miningType, 'Unrecognized')
		self.assertEqual(r.SourceCodeHandler.hasAutoDownload, False)
		self.assertEqual(r.SourceCodeHandler.hasPopUp, False)
		self.assertEqual(r.SourceCodeHandler.hasHiddenObject, False)
		self.assertEqual(r.SourceCodeHandler.hasNotification, True)
		self.assertEqual(r.SourceCodeHandler.hasHardwareAccess, {})

		self.assertLessEqual(r.BrowserSimulator.usage.mem, 2000)
		self.assertNotEqual(r.BrowserSimulator.viewfilename, "")

	def testRC1_6(self):
		# Scenario 1-6 - Successful enter a URL that has hidden objects and get result
		# Return valid result (find hidden objects)
		M = Model("https://www.google.com/")
		r = M.urlProcess("https://www.google.com/")

		self.assertEqual(r.BlacklistManager.maliciousType, 'safe URL')

		self.assertEqual(r.SourceCodeHandler.isMining, False)
		self.assertEqual(r.SourceCodeHandler.miningType, 'Unrecognized')
		self.assertEqual(r.SourceCodeHandler.hasAutoDownload, False)
		self.assertEqual(r.SourceCodeHandler.hasPopUp, False)
		self.assertEqual(r.SourceCodeHandler.hasHiddenObject, True)
		self.assertEqual(r.SourceCodeHandler.hasNotification, False)
		self.assertEqual(r.SourceCodeHandler.hasHardwareAccess, {})

		self.assertLessEqual(r.BrowserSimulator.usage.mem, 2000)
		self.assertNotEqual(r.BrowserSimulator.viewfilename, "")

	def testRC1_7(self):
		# Scenario 1-7 - Successful enter a URL that has mining script and get result
		# Return valid result (find mining)
		M = Model("http://dfcwecvmjtdj.com")
		r = M.urlProcess("http://dfcwecvmjtdj.com")

		self.assertEqual(r.BlacklistManager.maliciousType, 'safe URL')

		self.assertEqual(r.SourceCodeHandler.isMining, True)
		self.assertEqual(r.SourceCodeHandler.miningType, 'Unrecognized')#TODO
		self.assertEqual(r.SourceCodeHandler.hasAutoDownload, False)
		self.assertEqual(r.SourceCodeHandler.hasPopUp, False)
		self.assertEqual(r.SourceCodeHandler.hasHiddenObject, False)
		self.assertEqual(r.SourceCodeHandler.hasNotification, False)
		self.assertEqual(r.SourceCodeHandler.hasHardwareAccess, {})

		self.assertLessEqual(r.BrowserSimulator.usage.mem, 2000)
		self.assertNotEqual(r.BrowserSimulator.viewfilename, "")

	def testRC1_8(self):
		# Scenario 1-8 -  URL is not found in cache
		# Check in the database and return valid result
		M = Model("http://nigooglekbgo.xyz/uk/google22/5230/")
		r = M.urlProcess("http://nigooglekbgo.xyz/uk/google22/5230/")

		self.assertEqual(r.BlacklistManager.maliciousType, 'SOCIAL_ENGINEERING')

	def testRC1_9(self):
		# Scenario 1-9 - URL is not found in cache and database
		# Check with the third party server and return valid result
		M = Model("https://www.google.com/")
		r = M.urlProcess("https://www.google.com/")

		self.assertEqual(r.BlacklistManager.maliciousType, 'safe URL')

	def testRC2(self):
		# Scenario 2 - Invalid URL
		# Display error message
		M = Model("https://www")
		r = M.validURL()

		self.assertEqual(r, "")

	def testRC3(self):
		# Scenario 3 - User quits
		# Stop Processing
		M = Model("https://www.google.com/")
		r = M.validURL()

		self.assertEqual(r, "http://www.google.com/")
	
	def testRC4(self):
		# Scenario 4 - third party server unavailable
		# Part of the system end and throw error

		# Can't crash the third party server. skip test
		pass
	