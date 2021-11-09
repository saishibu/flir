import pymysql
from syntheticPowerData import generate

conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()
cur.execute("SELECT DevID,maxS,seed FROM `DevInfo`;")
DevInfo = cur.fetchall()
# print(DevInfo)
for row in DevInfo:
  DevID = row[0]
  maxS = row[1]
  seed = row[2]

  print(DevID)
  print(maxS)
  print(seed)
  print(" ")

  power=generate(DevID,maxS,seed)
  print(power)
  
  cur.execute("INSERT INTO `syntheticPowerData` (`DevID`, `v`, `i`, `pf`, `p`, `q`, `s`, `status`, `seed`) VALUES (%(DevID)s, %(v)s, %(i)s, %(pf)s, %(p)s, %(q)s, %(s)s, %(status)s, %(seed)s);",power);
  conn.commit() 
