while True:
 n = int(input("enter number:\n"))
 for prime_num in range(2, n):
     for i in range(2, int(prime_num/2) + 1):
       if prime_num % i == 0:
        break 
     else:
         print(prime_num)