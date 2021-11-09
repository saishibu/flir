import random, math

def generate():
pf=round(random.uniform(0.7,1),2)
ang=math.acos(pf)
powerData={'v':round(random.uniform(110,230),2),'i':round(random.uniform(0,20),2),'pf':pf,'p':round(v*i*pf,3),'q':round(v*i*math.sin(ang),3),'s':round(math.sqrt((v*v*i*i*pf*pf)+(v*v*i*i*math.sin(ang)*math.sin(ang))),3)}
