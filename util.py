from timeit import default_timer as timer

def lexOptions(line):
	return line.split()[1:]

def cout(str):
	print(str, end = '')

def endline():
	print('')

def myStrNcmp(s1, s2, n):
	if len(s1) < n or len(s2) > len(s1) or len(s2) < n:
		return False
	else:
		return (s1[:len(s2)].lower() == s2.lower())	

class myUsage:
	def __init__(self):
		self.TotalTimeUsage = 0
		self.PeriodTimeUsage = 0
		self.timeBUF = 0

	def start(self):
		self.timeBUF = timer()

	def end(self):
		self.PeriodTimeUsage = timer() - self.timeBUF
		self.TotalTimeUsage += self.PeriodTimeUsage

	def getTotalTime(self):
		return self.TotalTimeUsage

	def getPeriodTime(self):
		return self.PeriodTimeUsage
