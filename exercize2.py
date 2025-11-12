while True:
  n=int(input("Enter Number:\n"))
  for i in range(2, n+1):
     if n%i==0:
      print(i)