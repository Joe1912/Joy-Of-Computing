n=input()
for i in n:
  if(i.isupper()):
    k=i.lower()
  else:
    k=i.upper()
  print(k,end="")