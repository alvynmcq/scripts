# get application install failures and dump to .csv file
# to use "python install_failed.py > failed.csv "
import os
import sys

path_name = "\\\\3420094-dc01\RMPackageControl"

def get_fails():
	listdir = os.listdir(path_name)
	for f in listdir:
		if f.endswith(".ini"):
			listing = open(path_name + "\\" +f, "r", encoding="utf8")
			for line in listing:
				if "FAILED" in line:
					print(f + "," + line)
			listing.closed	

# run from command line
if __name__ =="__main__":

	get_fails()
