while True:
 x= int(input("enter  first number:\n"))
 y = int(input("enter second number:\n"))

 common_divisors = [i for i in range(1, min(x, y) + 1) if x % i == 0 and y % i == 0]

 print("comman_divisors:")
 print(common_divisors)