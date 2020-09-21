import os
from glob import glob

def doAll(folder):
	files = glob(folder+"*")
	for file in files:
		if os.path.isfile(file):
			if "bed.gz" in file:
				os.system("gunzip "+file)
			else:
				os.system("rm "+file)
		else:
			doAll(file+"/")

if __name__ == "__main__":
	folders = glob("*/")
	for folder in folders:
		doAll(folder)
