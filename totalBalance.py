from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed
import time, pymysql
url="http://sai-iota.duckdns.org:14265"
conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()
cur.execute("SELECT DevID,seed FROM `DevInfo`;")
DevInfo=cur.fetchall()
for row in DevInfo:
  DevID = row[0]
  seed = row[1]
  api = Iota(url,seed)
  input = api.get_inputs(start=0, stop=10)
  totalbalance=input['totalBalance']
  print(totalbalance)
  data={'totalbalance':totalbalance,'DevID':DevID,'seed':seed}
  cur.execute("INSERT INTO `totalBalance` ( `DevID`, `seed`, `totalbalance`) VALUES (%(DevID)s,%(seed)s,%(totalbalance)s);",data)
  conn.commit()
