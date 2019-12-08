import unittest
from src.SourceCodeHandler.SourceCodeHandler import SourceCodeHandler



class SourceCodeHandlerTest(unittest.TestCase):

	

	def test_parse(self):

		s = SourceCodeHandler("https://2.python-requests.org//zh_CN/latest/user/quickstart.html")
		s.parse()
		# self.assertEqual(s, 'FOO')

