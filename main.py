import argparse
from util import *
import gSet

def usage():
	print("Usage: [-File <doFile>]")

def myexit():
	usage()
	exit()

#gSet.myCmd = CmdParser("Classification")
gSet.init_global()

if( not gSet.myCmd.registerCommonCmd()):
	print("Register Common cmd failed")
	exit()

parser = argparse.ArgumentParser(description='')
parser.add_argument('-File', type=str, default='', help = '[-File <file>]')
args = parser.parse_args()

def main(_):
	if(args.File != ''):
		if gSet.myCmd.openDofile(args.File) == False:
			myexit()
	status = True
	while status != False:
		status = gSet.myCmd.executeOneCmd()

if __name__ == '__main__':
	main(1)


