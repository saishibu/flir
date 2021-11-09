import pymysql
from syntheticPowerData import generate

conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()
cur.execute("SELECT DevID,maxS,seed FROM `DevInfo` ORDER BY `DevInfo`.`ID` ASC")
DevInfo = cur.fetchall()
for row in DevInfo:
  DevID = DevInfo[0]
  maxS = DevInfo[1]
  seed = DevInfo[2]

print(DevID)
print(maxS)
print(seed)
print(" ")
# power=generate(DevID[1][0],maxS[1][0],seed[1][0])
# print(power)
# print(DevID[0][0])
# cur.execute("INSERT INTO `syntheticPowerData` (`DevID`, `v`, `i`, `pf`, `p`, `q`, `s`, `status`, `seed`) VALUES (%(DevID)s, %(v)s, %(i)s, %(pf)s, %(p)s, %(q)s, %(s)s, %(status)s, %(seed)s);",power);
# conn.commit() 
