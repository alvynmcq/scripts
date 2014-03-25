# Collects serial numbers from C2K machines
# To get a csv of details - python serial.py > serials.csv
import sys
import wmi
import subprocess

# Define DENI# of school
deni = "3420094"

# pings computers and then gets serial number
def serial():
	command = ['ping', '-n', '1', station]
	response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if response == 0:
		try:
			#num_serial()
			c = wmi.WMI(station)
			for i in c.Win32_ComputerSystem():
				compname = i.Name
			for x in c.Win32_Bios():
				serial = x.SerialNumber
			#print list to screen
			print ("%s , %s" % (compname, serial))
		except:
			print ("Station # " + station + " not working")
	else:
		print("Station # " + station + " switched off.")

# Generate station numbers from range and run ping to query - station 111 is crapping out with RPC not available error?
for num in range(1, 146):
	if num < 10:
		station = deni+'-STN00'+str(num)
		serial()
	elif num >= 10 and num <100:
		station = deni+'-STN0'+str(num)
		serial()
	else:
		station = deni+'-STN'+str(num)
		serial()
