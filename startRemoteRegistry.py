import os
import sys
import subprocess

def workstationList():
    for num in range(1, 200):
        if num < 10:
            station = deni+'-MST00'+str(num)
            station_num.append(station)
        elif num >= 10 and num < 100:
            station = deni+'-MST0'+str(num)
            station_num.append(station)
        else:
            station = deni+'-MST'+str(num)
            station_num.append(station)

def startService(workstation):
    start = subprocess.call("%s %s %s" % ('sc', workstation, 'start remoteregistry'))
    print(start)

def stopService(workstation):
    start = subprocess.call("%s %s %s" % ('sc', workstation, 'stop remoteregistry'))
    print(start)

def restartService(workstation):
    start = subprocess.call("%s %s %s" % ('sc', workstation, 'restart remoteregistry'))
    print(start)

def deleteProfile(workstation):
    delProf = subprocess.call([r'//3230310-FS01/Staff/delprof2.exe', '/c:'+workstation])
    print(delProf)

def main():
    workstationList()
    for s in station_num:
        wkstation = s
        startService(wkstation)
        deleteProfile(wkstation)

if __name__=="__main__":
    main()
