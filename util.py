
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
