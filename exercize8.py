while True:
 n= int(input("enter first number: "))
 m= int(input(" enter second number:"))
 p= input("choice the even or odd: ")

 print("result:")
 if p== "even":
     for i in range(n, m+ 1):
         if i % 2 == 0:
             print(i)
 elif p =="odd":
     for i in range(n, m + 1):
         if i % 2 != 0:
             print(i)
 else:
     print("error")