import unittest
from django.test import TestCase
from Blacklist.BlacklistManager import BlacklistManager
from Blacklist.BlacklistManager import BlacklistResult

class BlacklistManagerTest(TestCase):
	fixtures = ['blacklistDB.json']

	def testBlacklistManagerCheckWithMaliciousURL(self):
		self.bm = BlacklistManager("http://nigooglekbgo.xyz/uk/google22/5230/")
		self.result = self.bm.check()
		self.assertIsInstance(self.result, BlacklistResult)
		self.assertEqual(self.result.maliciousType, "SOCIAL_ENGINEERING")

	def testBlacklistManagerCheckWithSafeURL(self):
		self.bm = BlacklistManager("http://google.com")
		self.result = self.bm.check()
		self.assertIsInstance(self.result, BlacklistResult)
		self.assertEqual(self.result.maliciousType, "SOCIAL_ENGINEERING")

	def testCacheCheck(self):
		self.bm = BlacklistManager("http://google.com")
		self.bm.check()
		self.result = self.bm.checkCache()
		self.assertEqual(self.result, "safe URL")

	def testDBCheckWithExistedURL(self):
		self.bm = BlacklistManager("http://nigooglekbgo.xyz/uk/google22/5230/")
		self.result = self.bm.checkDB()
		self.assertEqual(self.result, "SOCIAL_ENGINEERING")

	def testDBCheckWithUnexistedURL(self):
		self.bm = BlacklistManager("http://google.com")
		self.result = self.bm.checkDB()
		self.assertEqual(self.result, "")

	def testThirdPartyCheck(self):
		self.bm = BlacklistManager("http://nigooglekbgo.xyz/uk/google22/5230/")
		self.result = self.bm.checkThirdParty()
		self.assertEqual(self.result, "SOCIAL_ENGINEERING")

	def testThirdPartyCheckError(self):
		self.bm = BlacklistManager("http://google.com")
		self.result = self.bm.checkThirdParty()
		self.assertEqual(self.result, "")