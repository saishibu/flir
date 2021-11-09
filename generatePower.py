import pymysql
from syntheticPowerData import generate

conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()
cur.execute("SELECT DevID FROM `DevInfo` ORDER BY `DevInfo`.`ID` ASC")
DevID = cur.fetchall()
cur.execute("SELECT seed FROM `DevInfo` ORDER BY `DevInfo`.`ID` ASC")
seed = cur.fetchall()
print(DevID)
print(seed)
power=generate(1,5000,0)
print(power)
