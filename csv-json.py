import csv
import json

csvfile = open('serial.csv', 'r')
jsonfile = open('serial.json', 'w')

fieldnames = ("StationNumber","SerialNumber")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
	json.dump(row, jsonfile, sort_keys=True, indent=2)
	jsonfile.write('\n')