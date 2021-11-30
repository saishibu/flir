#!/usr/bin/python3

import random, math, pymysql
from datetime import datetime, time

conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()

# 1 - DER
# 	Time 12am to 11:59pm
# 	Intermitted power cuts
# 	max capacity - 15kW self generation + from external souces
# 	Generate 10kW from Solar and 5kW from Wind
# 	Export excess to Battery or EV(through Charger)

if time(10,30) <= datetime.now().time() <= time(16,30):
  H_ThDER = 15 #Wind + Solar
  L_ThDER = 5
else:
  H_ThDER = 5 #Wind Only
  L_ThDER = 0
PDER = round(random.uniform(L_ThDER,H_ThDER),2)
print('DER')
print(PDER)

# 2 - Home With Solar
# 	Time 12am to 11:59pm
# 	Generation from 8am to 6pm
# 	Capacity - 2kW
# 	Consumption max 3kW
# 	Export excess to DER
# 	Climate affect solar production
# 	Import power from DER when more power required
# 	Export at Rs. 2 PU and Import at Rs. 4 PU

if time(10,30) <= datetime.now().time() <= time(16,30):
  H_ThH = 2 #
  L_ThH = 0
else:
  H_ThH = 0 
  L_ThH = 0
print('Home W solar')
PHWSImport = round(random.uniform(L_ThH,3),2)
PHWSExport = round(random.uniform(L_ThH,H_ThH),2)
PHWSTotal = round(PHWSImport-PHWSExport,2)
if PHWSTotal < 0:
  print("Exporting")
else:
  print("Importing")

print('Home Wo Solar')  
print(PHWSTotal)
print(PHWSImport)
print(PHWSExport)

# 3 - Home Without Solar
# 	Time 12am to 11:59pm
# 	Import power from DER
# 	Consumption Max 3kW
# 	Import at Rs. 4PU
PHWOSImport = round(random.uniform(2,3),2)
print(PHWOSImport)

# 4 - Charger
# 	Time 12am to 11:59pm
# 	Import power from DER
# 	Import at Rs. 20PU
# 	Max 10kW

Charger = round(random.uniform(3,10),2)
print(Charger)

# 5 - EV
# 	Import power from Charger
# 	Import at Rs. 25PU
# 	Max 10kW
print('EV')
EV = round(Charger*1.3 ,2)
print(EV)

# 6 - Factory
# 	Time 9am to 6pm
# 	Generation 10kW
# 	Import power from DER
# 	Import at Rs. 10PU
# 	Max 10kW

if time(9,00) <= datetime.now().time() <= time(10,30):
  H_ThFE = 0 #Solar High Th
  L_ThFE = 0 #Solar Low Th
  L_ThF = 10 #Import High Th
  L_ThF = 0 #Import Low Th
elif time(10,31) <= datetime.now().time() <= time(4,30):
  H_ThFE = 5 #Solar High Th
  L_ThFE = 0 #Solar Low Th
  L_ThF = 4.5 #Import High Th
  L_ThF = 0 #Import Low Th
else:
  H_ThFE = 0 #Solar High Th
  L_ThFE = 0 #Solar Low Th
  H_ThF = 0 #Import High Th
  L_ThF = 0 #Import Low Th
print('F')
FImport = round(random.uniform(L_ThFE,H_ThFE),2)
FExport = round(random.uniform(L_ThF,H_ThF),2)
FTotal = round(FImport-FExport,2)
print(FTotal)
# 7 - Battery
# 	Import and Export power from DER
# 	Import and Export at Rs. 3 PU
# 	Max capacity - 10kW
print('B')
BImport = round(random.uniform(0,10),2)
BExport = round(random.uniform(0,10),2)
BTotal = round(BImport-BExport,2)
print(BTotal)
# 8 - Solar Park
# 	Time 8am to 6pm
# 	Capacity - 10kW
# 	Export power to DER
# 	Climate affects performance
# 	Export at Rs. 3 PU
print('SP')
if time(10,30) <= datetime.now().time() <= time(16,30):
  H_ThSP = 2 #
  L_ThSP = 0
else:
  H_ThSP = 0 
  L_ThSP = 0

SPExport = round(random.uniform(L_ThH,H_ThH),2)
print(SPExport)
data ={ 'PDER':PDER,'PHWSImport':PHWSImport,'PHWSExport':PHWSExport, 'PHWSTotal':PHWSTotal, 'PHWOSImport':PHWOSImport, 'Charger':Charger, 'EV':EV, 'FImport':FImport, 'FExport':FExport, 'FTotal':FTotal, 'BImport':BImport, 'BExport':BExport, 'BTotal':BTotal, 'SPExport':SPExport }
cur.execute("INSERT INTO `newSyntheticPowerData` (`PDER`, `PHWSImport`, `PHWSExport`, `PHWSTotal`, `PHWOSImport`, `Charger`, `EV`, `FImport`, `FExport`, `FTotal`, `BImport`, `BExport`, `BTotal`, `SPExport`) VALUES (%(PDER)s, %(PHWSImport)s, %(PHWSExport)s, %(PHWSTotal)s, %(PHWOSImport)s, %(Charger)s, %(EV)s, %(FImport)s, %(FExport)s, %(FTotal)s, %(BImport)s, %(BExport)s, %(BTotal)s, %(SPExport)s );",data)
conn.commit()
