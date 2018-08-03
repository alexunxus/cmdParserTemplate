import readline
from commonCmd import *

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')



class CmdParser:
	def __init__(self, prompt_name):
		self.prompt		= prompt_name	  # define prompt name
		self.buffer		= ''			  # to temporarily store the current command
		self.cmdDict	= {}
		self.doLines	= []
		self.doPtr		= 0

	def printPrompt(self):
		cout(self.prompt+"> ")

	def getPromptStr(self):
		return self.prompt+"> "

	def parse(self, line):
		self.buffer = copy(line)
		return True

	def executeOneCmd(self):
		line = ''
		if len(self.doLines)>0:
			if self.doPtr == len(self.doLines):
				self.doLines = []
				self.doPtr = 0
				line = (input(self.getPromptStr()))
			else:
				line = self.doLines[self.doPtr]
				self.doPtr += 1
				self.printPrompt()
				print(line)
		else:
			line = (input(self.getPromptStr()))
		cmd = self.RegCmd(line.split()[0])
		if cmd!=None:
			if cmd.isQuitCmd():
				print('\n')
				return False
			cmd.execute(line)
		else:
			print("Unknown command \""+line.split()[0]+"\"\n")
		return True

	def RegCmd(self, cmd):
		for key in self.cmdDict.keys():
			if(self.cmdDict[key].isCmd(cmd)):
				return self.cmdDict[key]
		return None

	def openDofile(self, dofile):
		try:
			f = open(dofile, 'r')
		except IOError:
			print("File \""+dofile+"\" cannot be opened!")
			return False
		for line in f:
			line = line.strip()
			if(line != ''):
				self.doLines.append(line)
				readline.add_history(line)
		self.doPtr = 0
		f.close()
		return True

	def registerCommonCmd(self):
		self.cmdDict['HIStory'] = HistoryCmd()
		self.cmdDict['DOfile']	= DofileCmd()
		self.cmdDict['Quit']	= QuitCmd()
		self.cmdDict['HELp']	= HelpCmd()
		return True

