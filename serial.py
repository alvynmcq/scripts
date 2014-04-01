# python serial.py <DENI #> <machine designator i.e. STN, TLP, STS etc.> <first station number> <last station number>
# Collects serial numbers from C2K machines
# To get a csv of details - python serial.py > serials.csv 
import csv
import sys
import wmi
import subprocess

# command line arguments deni, station designation, first machine, last machine
deni = sys.argv[1]
sticker = sys.argv[2]
first = int(sys.argv[3])
last = int(sys.argv[4])
station_num=[]

# Generate station numbers from range and save to station_num list
def station_number(school):
	for num in range(first, last):
		if num < 10:
			station = deni+'-'+sticker+'00'+str(num)
			station_num.append(station)
		elif num >= 10 and num <100:
			station = deni+'-'+sticker+'0'+str(num)
			station_num.append(station)
		else:
			station = deni+'-'+sticker+str(num)
			station_num.append(station)
	
def serial(target):
	try:
		c = wmi.WMI(station)
		for i in c.Win32_ComputerSystem():
			compname = i.Name
		for x in c.Win32_Bios():
			serial = x.SerialNumber
		print ("%s,%s" % (compname, serial))
	except:
		print("Station # " + station + " switched off.")

if __name__=="__main__":
	station_number(sys.argv[1:])
	for s in station_num:
		station = s
		serial(s)


		
