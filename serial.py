# Collects serial numbers from C2K machines
import sys
import wmi
import json
import subprocess
# Empty list for station and serial #
detail_list = []
# Define DENI# of school
deni = "3420094"
# Make sure windows can see wmi stuff
if "C:\\Python33" not in sys.path:
	sys.path.append("C:\\Python33")

# function to query machine and retrieve computer name and serial number
def num_serial():
	c = wmi.WMI(station)
	for i in c.Win32_ComputerSystem():
		compname = i.Name
	for x in c.Win32_Bios():
		serial = x.SerialNumber
	#push machine details to list	
	detail_list.extend((compname, serial))
	#push list to dictionary
	detail_dict = dict(zip(detail_list[0::2], detail_list[1::2]))
	#print list to screen
	print ("Station #: %s Serial # :%s" % (compname, serial))
	#dump json for possible angularjs jiggery pokery
	with open('basic.json', mode='w', encoding='utf-8') as f:
		json.dump(detail_dict, f, sort_keys=True, indent=2)

# function to ping computer to make sure it is alive and then run num_serial()
def ping():
	command = ['ping', '-n', '1', station]
	response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if response == 0:
		try:
			num_serial()
		except:
			print ("Station # " + station + " not working")
	else:
		print("Station # " + station + " switched off.")

# Generate station numbers from range and run ping to query - station 111 is crapping out with RPC not available error?
for num in range(1, 146):
	if num < 10:
		station = deni+'-STN00'+str(num)
		ping()
	elif num >= 10 and num <100:
		station = deni+'-STN0'+str(num)
		ping()
	else:
		station = deni+'-STN'+str(num)
		ping()
