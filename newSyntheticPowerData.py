import random, math, pymysql
from datetime import datetime, time

# 1 - DER
# 	Time 12am to 11:59pm
# 	Intermitted power cuts
# 	max capacity - 15kW self generation + from external souces
# 	Generate 10kW from Solar and 5kW from Wind
# 	Export excess to Battery or EV(through Charger)

if time(10,30) <= datetime.now().time() <= time(16,30):
  H_ThDER = 15 #Wind + Solar
  L_ThDER = 5
  print(datetime.now().time())
else:
  H_ThDER = 5 #Wind Only
  L_ThDER = 0
  print(datetime.now().time())
PDER = round(random.uniform(L_ThDER,H_ThDER),2)

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

# 3 - Home Without Solar
# 	Time 12am to 11:59pm
# 	Import power from DER
# 	Consumption Max 3kW
# 	Import at Rs. 4PU

# 4 - Charger
# 	Time 12am to 11:59pm
# 	Import power from DER
# 	Import at Rs. 20PU
# 	Max 10kW

# 5 - EV
# 	Import power from Charger
# 	Import at Rs. 25PU
# 	Max 10kW

# 6 - Factory
# 	Time 9am to 6pm
# 	Generation 10kW
# 	Import power from DER
# 	Import at Rs. 10PU
# 	Max 10kW

# 7 - Battery
# 	Import and Export power from DER
# 	Import and Export at Rs. 3 PU
# 	Max capacity - 10kW

# 8 - Solar Park
# 	Time 8am to 6pm
# 	Capacity - 10kW
# 	Export power to DER
# 	Climate affects performance
# 	Export at Rs. 3 PU
