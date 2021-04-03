n, B = list(map(int, input().strip().split()))
T = 0

# your code here
total=0
for guess in range(1,n+1):
  if guess % 2 == 1 :
    pn = 3**guess + 1
    total+=pn**(n-guess)
  elif guess % 2 == 0 :
    pn = 2**guess + 1
    total+=pn**(n-guess)
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

if high==int(low)+1==10000 < B:
  T = -1
else:
  if (int(T)+1)*total<B:
    T=T2
  if T % 1 == 0:
    T = T
  else:
    T =int(T)+1
  
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)





