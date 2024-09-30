# ecef_to_sez.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour
#  Conversion from year, month, day, hour, minute, second to fractional Julian date
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
# Output:
#  Fractional Julian date
#
# Written by Timothy McEvoy
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import sys # argv
import math # math module

# "constants"


# initialize script arguments
year = float('nan') # x in ECEF origin of the SEZ frame
month = float('nan') # y in ECEF origin of the SEZ frame
day = float('nan') # z in ECEF origin of the SEZ frame
hour = float('nan') # x ECEF position
minute = float('nan') # y ECEF position
second = float('nan') # z ECEF position

# parse script arguments
if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 ymdhms_to_jd.py year month day hour minute second'\
        )
    exit()

# script below this line

jd=day-32075+1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
jd_mid=jd-0.5
d_frac=(second+60*(month+60*hour))/86400
jd_frac=jd_mid+d_frac
print(jd_frac)