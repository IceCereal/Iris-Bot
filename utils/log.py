"""
	A logging utility. It will handle logging for Iris.

	Author: IceCereal
"""
from argparse import ArgumentParser
from json import dump, load
from pathlib import Path

class Logger:
	def __init__(self, resPath : Path, verbose : bool = None):
		if (verbose):
			print ("Entering Class: Logger")
			print ("resPath:\t", resPath)

		self.resPath = resPath
		self.verbose = verbose

if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument('-v', "--verbose", required=False, help="Run log.py with verbosity")
	args = parser.parse_args()

	if args.verbose == "True":
		args.verbose = True
	else:
		args.verbose = None

	if (args.verbose):
		print ("Entered log.py")
	
	if (args.verbose):
		print ("Creating instance of logger with resPath as \"res\"...")
	
	log = Logger(resPath = Path("res"), verbose = args.verbose)