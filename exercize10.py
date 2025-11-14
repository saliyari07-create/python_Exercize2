while True:
    
    print("1. تبدیل ده‌دهی به دودویی")
    print("2. تبدیل دودویی به ده‌دهی")
    
    
    choice = input( "choice 1 orr 2:\n")
    
    if choice == "1":
     
        num = int(input("enter decimal_number\n"))
        n = num
        binary = ""
        
        if num == 0:
            binary = "0"
        else:
            while num > 0:
                remainder = num % 2
                binary = str(remainder) + binary
                num //= 2
        
        print(f"{n} در مبنای دودویی برابر است با: {binary}")
    
    elif choice == "2":
       
        binary = input("enter binary_number:\n")
        
        valid = True
        for bit in binary:
            if bit not in "01":
                valid = False
                break
        
        decimal = 0
        power = len(binary) - 1
        for bit in binary:
            decimal += int(bit) * (2 ** power)
            power -= 1
        
        print(f"{binary} در مبنای ده‌دهی برابر است با: {decimal}")
    