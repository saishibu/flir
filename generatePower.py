import pymysql
from syntheticPowerData import generate

conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()
cur.execute("SELECT DevID,seed FROM `DevInfo` ORDER BY `DevInfo`.`ID` ASC")
DevInfo = cur.fetchall()
DevID = DevInfo[0]
seed = DevInfo[1]
print(DevID)
print(seed)
power=generate(1,5000,0)
print(power)
