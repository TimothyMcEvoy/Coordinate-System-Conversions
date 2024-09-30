# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef with o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Converts sez reference frame to ecef
# Parameters:
#  o_lat_deg: lattitude angle in degrees
#  o_lon_deg: longtitude angle in degrees
#  o_hae_km: Height above earth in km -- hae is actually not necessary at all because we have these other variables!
#  s_km: s component
#  e_km: e component
#  z_km: z component
#  ...
# Output:
#  ECEF vectors
#
# Written by Timothy McEvoy
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math # math module

# "constants"
# e.g., R_E_KM = 6378.137
RE = 6378.1363  # km
eE = 0.081819221456  # eccentricity

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
o_lat_deg = float('nan') # Lattitude in SEZ
o_lon_deg = float('nan') # Longtitude in SEZ
o_hae_km = float('nan') # Altitude in SEZ
s_km = float('nan') # s component in SEZ
e_km = float('nan') # e component in SEZ
z_km = float('nan') # z component in SEZ

# parse script arguments
if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km = float(sys.argv[3])
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 sez_to_ecef.py Lat Lon HAE S E Z'\
        )
    exit()

# write script below this line


#Convert to rads
o_lat_rad = o_lat_deg*(math.pi/180)
o_lon_rad = o_lon_deg*(math.pi/180)

#ECEF basis vector
x_basis = math.cos(o_lon_rad)*math.sin(o_lat_rad)*s_km+math.cos(o_lon_rad)*math.cos(o_lat_rad)*z_km-math.sin(o_lon_rad)*e_km
y_basis = math.sin(o_lon_rad)*math.sin(o_lat_rad)*s_km+math.sin(o_lon_rad)*math.cos(o_lat_rad)*z_km+math.cos(o_lon_rad)*e_km
z_basis = -math.cos(o_lat_rad)*s_km+math.sin(o_lat_rad)*z_km

# Calculating CE and SE
CE = RE / math.sqrt(1 - pow(eE, 2) * pow(math.sin(o_lat_rad), 2))
SE = (RE * (1 - pow(eE, 2))) / math.sqrt(1 - pow(eE, 2) * pow(math.sin(o_lat_rad),2))

# Calculating rx, ry, rz
r_x_km = (CE + o_hae_km) * math.cos(o_lat_rad) * math.cos(o_lon_rad)
r_y_km = (CE + o_hae_km) * math.cos(o_lat_rad) * math.sin(o_lon_rad)
r_z_km = (SE + o_hae_km) * math.sin(o_lat_rad)

#Determine ECEF vector
ecef_x_km = x_basis+r_x_km
ecef_y_km = y_basis+r_y_km
ecef_z_km = z_basis+r_z_km

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)