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
power=generate(DevID[0],5000,seed[0])
print(power)
cur.execute("INSERT INTO `syntheticPowerData` (`DevID`, `v`, `i`, `pf`, `p`, `q`, `s`, `status`, `seed`) VALUES (%(DevID)s, %(v)s, %(i)s, %(pf)s, %(p)s, %(q)s, %(s)s, %(status)s, %(seed)s);",power);
conn.commit() 
