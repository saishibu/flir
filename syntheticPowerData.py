import random, math, pymysql

def generate(DevID,maxS,seed):
  pf = round(random.uniform(0.7,1),2)
  ang = math.acos(pf)
  v = round(random.uniform(110,230),2)
  i = round(random.uniform(0,20),2)
  p = round(v*i*pf,3)
  q = round(v*i*math.sin(ang),3)
  s = round(math.sqrt(p*p+q*q),3)
  status = ""
  if s>maxS:
    status = "OL"
  powerData={'id':DevID,'v':v,'i':i,'pf':pf,'p':p,'q':q,'s':s,'status':status,'seed':seed}
  return(powerData)
  
