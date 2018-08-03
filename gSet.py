from cmdParser import CmdParser
from util import myUsage

def init_global():
	global myCmd 
	myCmd = CmdParser("cmd")
	global myUsg
	myUsg = myUsage()
