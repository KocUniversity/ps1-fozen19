n= 4
total=0
T=0
B=1179881
while T < 10000 and total < B:
  for guess in range(1,n+1):
    if guess % 2 == 1 :
      pn = 3**guess + 1
      total+=pn**(n-guess)
    elif guess % 2 == 0 :
      pn = 2**guess + 1
      total+=pn**(n-guess)
  T+=1
print(total)
if total < B:
  T= -1
else:
  T=T
print(T)
for guess in range(1,n+1):
  if guess % 2 == 1 :
    pn = 3**guess + 1
    total+=pn**(n-guess)
  elif guess % 2 == 0 :
    pn = 2**guess + 1
    total+=pn**(n-guess)
print(total)
low = 0
high = 10000
T = (low + high)/2
T2 = 0
while abs(T*total-B)>0:
  
  if T*total > B:
    T2=(low + high)/2
    high = T 
  elif T*total < B :
    low = T
  if abs(high-low)<1:
    break
  T = (high +low)/2
  print(T)
if 10000*total < B:
  T=-1
else:
  if (int(T)+1)*total<B:
    T=T2

  if T % 1 == 0:
    T = T
  else:
    T =int(T)+1
print(T)


    
   


