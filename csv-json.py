import csv
import sys
import json

def csvToJson(csvfile):
	csv_filename = csvfile[0]
	print("Opening .csv file: ",csv_filename)
	csvfile = open(csv_filename, 'r')
	reader = csv.DictReader(csvfile)

	json_filename = csv_filename.split(".") [0]+".json"
	print("Saving .json to file: ",json_filename)
	jsonfile = open(json_filename, 'w')
    
	for row in reader:
	    json.dump(row, jsonfile, sort_keys=True, indent=2)
	    jsonfile.write('\n')

	csvfile.close()
	jsonfile.close()

if __name__=="__main__":
	csvToJson(sys.argv[1:])
