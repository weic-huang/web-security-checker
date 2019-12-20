import unittest
from src.SourceCodeHandler.SourceCodeHandler import SourceCodeHandler



class SourceCodeHandlerTest(unittest.TestCase):

	

	def test_parse(self):

		s = SourceCodeHandler("https://www.mobile01.com/topicdetail.php?f=37&t=5886669")
		s.parse()
		# self.assertEqual(s, 'FOO')

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

                s = SourceCodeHandler("")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasAutoDownload'], True)

                s = SourceCodeHandler("")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasPopUp'], True)

                s = SourceCodeHandler("https://kkplay3c.net/141126-2/")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasNotification'], True)

                s = SourceCodeHandler("https://davidwalsh.name/demo/camera.php")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasHardwareAccess']['camera'], True)

                s = SourceCodeHandler("https://addpipe.com/simple-web-audio-recorder-demo/")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasHardwareAccess']['microphone'], True)

                s = SourceCodeHandler("")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasHardwareAccess']['Ambient Light Sensor'], True)

                s = SourceCodeHandler("")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasHardwareAccess']['Device Motion'], True)

                s = SourceCodeHandler("")
                s.parse()
                result = s.callJSScanner()
                self.assertEqual(result['hasHardwareAccess']['Device Orientation'], True)

        def test_callHtmlScanner(self):

                s = SourceCodeHandler("https://www.tutorialrepublic.com/css-tutorial/css-visibility.php")
                s.parse()
                result = s.callHtmlScanner()
                self.assertEqual(result, True)

                s = SourceCodeHandler("https://www.google.com/")
                s.parse()
                result = s.callHtmlScanner()
                self.assertEqual(result, False)
