import sys
import os
import string

# URLs have this format
# https://nomads.ncep.noaa.gov:443/dods/gefs/gefs20201207/gefs_pgrb2ap5_all_00z.ascii?tmp2m[0:30][0:64][255][560]
# $URLBASE $DATE $QUERYPREFIX $TIME $QUERYPOSTFIX $VARIABLE $RANGE1 $RANGE2 $LAT $LON
# URLBASE: https://nomads.ncep.noaa.gov:443/dods/gefs/gefs
# DATE: 20201207
# QUERYPREFIX: /gefs_pgrb2ap5_all_
# TIME: 00z
# QUERYPOSTFIX: .ascii?
# VARIABLE: tmp2m
# RANGE1: [0:30]
# RANGE2: [0:64]
# LAT: [255]
# LON: [560]

URLBASE = 'https://nomads.ncep.noaa.gov:443/dods/gefs/gefs'
QUERYPREFIX = '/gefs_pgrb2ap5_all_'
TIME = [ '00z', '06z', '12z', '18z' ]
QUERYPOSTFIX = '.ascii?'
VARIABLE = [ 'tmp2m', 'pressfc', 'rh2m', 'dlwrfsfc', 'dswrfsfc', 'apcpsfc', 'ugrd10m', 'vgrd10m' ]
RANGE1 = '[0:30]'
RANGE2 = '[0:64]'

def GenList(lat, lon, date):
    urllist = []
    for i in range(0,len(TIME)):
        for j in range(0,len(VARIABLE)):
            url = URLBASE + DATE + QUERYPREFIX + TIME[i] + QUERYPOSTFIX + VARIABLE[j] + RANGE1 + RANGE2 + LAT + LON
            urllist.append(url)
    return urllist

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: " + sys.argv[0] + "base_directory date lat lon\n")
        print("Example: " + sys.argv[0] + " /opt/flare 20201207 255 560\n")
    else:
        LAT = '[' + str(sys.argv[3]) + ']'
        LON = '[' + str(sys.argv[4]) + ']'
        DATE = str(sys.argv[2])
        urllist = GenList(LAT, LON, DATE)
        print(urllist)
