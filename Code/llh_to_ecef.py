# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
# Converts LLH to ECEF vector components
# Parameters:
#  Lon: Longtitude from LLH
#  Lat: Lattitude from LLH
#  HAE: Altitude from LLH
# Output:
#  ECEF Coordinates x, y, z
#
# Written by Timothy McEvoy
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import sys # argv
import math # math module

# "constants"
RE = 6378.1363  # km
eE = 0.081819221456  # eccentricity

# initialize script arguments
Lat = float('nan') # Lattitude in LLH
Lon = float('nan') # Longtitude in LLH
HAE = float('nan') # Altitude in LLH

# parse script arguments
if len(sys.argv)==4:
    Lat = float(sys.argv[1])
    Lon = float(sys.argv[2])
    HAE = float(sys.argv[3])
else:
    print(\
        'Usage: '\
        'python3 llh_to_ecef.py Lat Lon HAE'\
        )
    exit()

# script below this line

    # Calculating CE and SE
CE = RE / math.sqrt(1 - pow(eE, 2) * pow(math.sin(math.radians(Lat)), 2))
SE = (RE * (1 - pow(eE, 2))) / math.sqrt(1 - pow(eE, 2) * pow(math.sin(math.radians(Lat)),2))

    # Calculating rx, ry, rz
r_x_km = (CE + HAE) * math.cos(math.radians(Lat)) * math.cos(math.radians(Lon))
r_y_km = (CE + HAE) * math.cos(math.radians(Lat)) * math.sin(math.radians(Lon))
r_z_km = (SE + HAE) * math.sin(math.radians(Lat))

    # Printing Solution
print(r_x_km)
print(r_y_km)
print(r_z_km)