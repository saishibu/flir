from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed
import time, pymysql
url="http://sai-iota.duckdns.org:14265"
conn = pymysql.connect(host='localhost', user='sai', password='sheeba99', database='flir')
cur = conn.cursor()
cur.execute("SELECT seed FROM `DevInfo`;")
DevInfo=cur.fetchall()
for row in DevInfo:
  seed = row[0]
  api = Iota(url,seed)
  input = api.get_inputs(start=0, stop=10)
  totalbalance=input['totalBalance']
  print(totalbalance)
