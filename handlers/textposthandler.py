import sys
sys.path.append('..')
#import showmenu
import plugins.responses

#global variable
KEYWORDS = {u'天气' : 'getweather', u'温度' : 'gettemperature',}
PREFIX = {'1001' : 'repeatwords', '1002' : 'translate'}
MYSPLIT = '+'

class MyResponse:
	pass

class TextReqHandler:
	def __init__(self, req):
		self.touser = req.touser
		self.fromuser = req.fromuser
		self.createtime = req.createtime
		self.msgtype = req.msgtype
		self.msgid = req.msgid
		self.content = req.content
#--------------------------------------business section start-----------------------------------------------
	#define all business functions in this section
	#you must add you function to the global dictionary at the top
	
	def formatresp(self, resp):
		response = MyResponse()
		response.fromuser = self.touser
		response.touser = self.fromuser
		type = resp.type
		if type == '':
			pass
		elif type == '':
			pass
		elif type == '':
			pass
	#----------------------------------------business section end-----------------------------------------------
	
	#main function
	def getresponse(self):
		content = self.content
		global KEYWORDS
		global PREFIX
		global MYSPLIT
		try:
			#if keywords command
		    response = KEYWORDS[content]()
		except:
			try:
				#if prefix command
				prefix,realcontent = content.split(MYSPLIT, 1)
			except:
				#no match command
				errcode = '0'
				response = showmenu(errcode)
			else:
				try:
					#if right prefix
					response = PREFIX[prefix](realcontent)
				except:
					#no match prefix
					errcode = '1'
					response = showmenu(errcode)
		finally:
			response = formatresp(response)
			return response
			
#-----------------------------------------------common section start--------------------------------------------
#define all common functions in this section
#common function means function which can run without the class
#for example you can make a 'switch' function here
def getweather():
	pass
	
def gettemperature():
	pass
	
def repeatwords(words):
	pass
	
def translate(words):
	pass
#-----------------------------------------------common section end--------------------------------------------