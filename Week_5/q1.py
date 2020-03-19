import math
N,v1,v2=map(int,input().split())
walk_time=(math.sqrt(2)*N)/v1
cab_time=(2*N)/v2
if(v1==0):
  print("Cab",end="")
elif(v2==0):
  print("Walk",end="")
else:
  if(walk_time<=cab_time):
      print("Walk",end="")
  else:
      print("Cab",end="")