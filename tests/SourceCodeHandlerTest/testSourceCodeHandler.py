import unittest
from src.SourceCodeHandler.SourceCodeHandler import SourceCodeHandler



class SourceCodeHandlerTest(unittest.TestCase):

	

	def test_parse(self):

		s = SourceCodeHandler("https://www.mobile01.com/topicdetail.php?f=37&t=5886669")
		s.parse()
		# self.assertEqual(s, 'FOO')

