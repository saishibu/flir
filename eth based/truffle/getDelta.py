import pandas as pd

def deltaJson(): 
  excel_data = pd.read_excel('Optimization.xlsx','Sheet2')
  data = pd.DataFrame(excel_data)
  delta = {p1:float(data['P1']),p2:float(data['P2']),p3:float(data['P3']),p4:float(data['P4']),p5:float(data['P5'])}
  return delta
