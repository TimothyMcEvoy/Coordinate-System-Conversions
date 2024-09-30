# ecef_to_sez.py
#
# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
#  Converts ECEF reference frame to SEZ
# Parameters:
#  o_x_km x in ECEF origin of the SEZ frame
#  o_y_km y in ECEF origin of the SEZ frame
#  o_z_km z in ECEF origin of the SEZ frame
#  ...
# Output:
#  SEZ reference frame
#
# Written by Timothy McEvoy
# Other contributors: Brad Denby
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys # argv
import math # math module

# "constants"
R_E_KM = 6378.1363
e_E    = 0.081819221456

# initialize script arguments
o_x_km = float('nan') # x in ECEF origin of the SEZ frame
o_y_km = float('nan') # y in ECEF origin of the SEZ frame
o_z_km = float('nan') # z in ECEF origin of the SEZ frame
x_km = float('nan') # x ECEF position
y_km = float('nan') # y ECEF position
z_km = float('nan') # z ECEF position

# parse script arguments
if len(sys.argv)==7:
    o_x_km = float(sys.argv[1])
    o_y_km = float(sys.argv[2])
    o_z_km = float(sys.argv[3])
    x_km = float(sys.argv[4])
    y_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 ecef_to_sez.py o_x o_y o_z x y z'\
        )
    exit()

# write script below this line

#Get ECEF vector from origin to object
v_x_km = x_km - o_x_km
v_y_km = y_km - o_y_km
v_z_km = z_km - o_z_km

## Begin ECEF to LLH (from ecef_to_llh.py)
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))
# calculate longitude
lon_rad = math.atan2(o_y_km,o_x_km)
# initialize lat_rad, r_lon_km, r_z_km
lat_rad = math.asin(o_z_km/math.sqrt(o_x_km**2+o_y_km**2+o_z_km**2))
r_lon_km = math.sqrt(o_x_km**2+o_y_km**2)
prev_lat_rad = float('nan')
# iteratively find latitude
c_E = float('nan')
count = 0
while (math.isnan(prev_lat_rad) or abs(lat_rad-prev_lat_rad)>10e-7) and count<5:
  denom = calc_denom(e_E,lat_rad)
  c_E = R_E_KM/denom
  prev_lat_rad = lat_rad
  lat_rad = math.atan((o_z_km+c_E*(e_E**2)*math.sin(lat_rad))/r_lon_km)
  count = count+1
## End ECEF to LLH

# set up matricies for ECEF to SEZ conversions
Rz=[[math.sin(lat_rad),0,-math.cos(lat_rad)],[0,1,0],[math.cos(lat_rad),0,math.sin(lat_rad)]]
Ry=[[math.cos(lon_rad),math.sin(lon_rad),0],[-math.sin(lon_rad),math.cos(lon_rad),0],[0,0,1]]
RzRy=[[0,0,0],[0,0,0],[0,0,0]]
Recef=[[v_x_km],[v_y_km],[v_z_km]]
Rsez=[[0,0,0],[0,0,0],[0,0,0]]

# Multiply matricies to get RzRy from Rz*Ry
for i in range(len(Rz)):
   for j in range(len(Ry[0])):
       for k in range(len(Ry)):
           RzRy[i][j] += Rz[i][k] * Ry[k][j]
# Multiply matricies to get Rsez from RzRy*Recef
for i in range(len(RzRy)):
   for j in range(len(Recef[0])):
       for k in range(len(Recef)):
           Rsez[i][j] += RzRy[i][k] * Recef[k][j]

#Pulling SEZ results from matrix
s_km=Rsez[0][0]
e_km=Rsez[1][0]
z_km=Rsez[2][0]

#Printing results
print(s_km)
print(e_km)
print(z_km)