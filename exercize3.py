while True:
 x = int(input("enter number:\n"))
 if x <= 1:
      print("not prime")
 else:
    
    is_prime = True
    for i in range(2, int(x** 0.5) + 1):
        if x % i == 0:
            is_prime = False
           
            
    if is_prime:
        print("prime")
    else:
        print("not prime")