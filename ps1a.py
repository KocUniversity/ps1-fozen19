n, B = list(map(int, input().strip().split()))
T = 0

# your code here
total=0
while T < 10000 and total < B:
  for guess in range(1,n+1):
    if guess % 2 == 1 :
      pn = 3**guess + 1
      total+=pn**(n-guess)
    elif guess % 2 == 0 :
      pn = 2**guess + 1
      total+=pn**(n-guess)
  T+=1
if total < B:
  T=-1
else:
  T=T
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)