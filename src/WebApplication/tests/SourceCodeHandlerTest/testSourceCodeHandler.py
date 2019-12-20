import unittest
from SourceCodeHandler.SourceCodeHandler import SourceCodeHandler

class SourceCodeHandlerTest(unittest.TestCase):

        def test_callMiningChecker(self):

                s = SourceCodeHandler("https://bitcoin-russia.ru/")
                s.parse()
                result = s.callMiningChecker()
                self.assertEqual(result['isMining'], True)
                self.assertEqual(result['miningType'], "Unrecognized")

                s = SourceCodeHandler("https://www.google.com/")
                s.parse()
                result = s.callMiningChecker()
                self.assertEqual(result['isMining'], False)
                self.assertEqual(result['miningType'], "Unrecognized")

        def test_callJSScanner(self):

                s = SourceCodeHandler("https://kkplay3c.net/141126-2/")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasNotification'], True)

                s = SourceCodeHandler("https://davidwalsh.name/demo/camera.php")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasHardwareAccess']['camera'], True)

 
        def test_callHtmlScanner(self):

                s = SourceCodeHandler("https://www.google.com/")
                s.parse()
                result = s.callHtmlScanner()
                self.assertEqual(result["hasHiddenObject"], True)

                s = SourceCodeHandler("http://sample.com")
                s.parse()
                result = s.callHtmlScanner()
                self.assertEqual(result["hasHiddenObject"], False)