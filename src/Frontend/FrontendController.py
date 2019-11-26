import FrontendURL
import FrontendRsult

class FrontendController():
	def __init__(self):
		self.URL = getURL() #from Frontend URL
		self.result=[]
		self.displaystation="URLPage" # or ResultPage

	def displayControl(self):
		# display the web by displaystation
		pass

    def checkURL(self):
    	#check url existence
    	pass
    def setSocket(self):
		# build web Socket to the backend
        pass
    def listenSocket(self):
    	# listen the socket from the backend
    	pass
    def sendSocket(self):
        #send message to the backend
        pass  

      

