from util import *
import readline
import gSet

class ExeCmd:
	def __init__(self, name="Exename", n=0):
		self.exename = name
		self.nCompulsory = n
	def isCmd(self, cmd):
		return myStrNcmp(self.exename, cmd, self.nCompulsory)
	def execute(self, line):
		print(line, '\n')
		#print("Should not execute the virtual class ExeCmd!")
	
	def Usage(self):
		print("")
	def isQuitCmd(self):
		return False

class HistoryCmd(ExeCmd):
	def __init__(self):
		super(HistoryCmd, self).__init__("HIStory", 3)
	
	def execute(self, line):
		for index in range(readline.get_current_history_length()):
			print(index, ". ", str(readline.get_history_item(index)))
		print("")

	def Usage(self):
		print("HIStory: HIStory")

class DofileCmd(ExeCmd):
	def __init__(self):
		super(DofileCmd, self).__init__("DOfile", 2)
	
	def execute(self, line):
		line = lexOptions(line)
		if len(line) > 2:
			print("Extra argument \"", line[3],"\"")
		if len(line) == 1:
			gSet.myCmd.openDofile(line[0])
		if len(line) == 2:
			doReplace = False
			for i in line:
				if myStrNcmp("-Replace", i, 2):
					doReplace = True
			if not doReplace:
				print("Unknown argument \"", line, "\"")
				

	def Usage(self):
		print("DOfile: DOfile < file > [-Replace]")

class QuitCmd(ExeCmd):
	def __init__(self):
		super(QuitCmd, self).__init__("Quit", 1)
	
	def Usage(self):
		print("Quit: Quit [ -Force ]")

	def isQuitCmd(self):
		return True

class HelpCmd(ExeCmd):
	def __init__(self):
		super(HelpCmd, self).__init__( "HELp", 3)
	
	def execute(self, line):
		line = lexOptions(line)
		if len(line) > 1:
			print("Extra argument \"", line[1],"\"")
		if len(line) == 1:
			cmdexe = gSet.myCmd.RegCmd(line[0])
			if cmdexe ==None:
				print("Unknown command \"", line[0], "\"")
			else:
				cmdexe.Usage()
			endline()

		else:
			for key in gSet.myCmd.cmdDict.keys():
				gSet.myCmd.cmdDict[key].Usage()
			endline()

	def Usage(self):
		print("HELp: HELp [ command ]")
	
