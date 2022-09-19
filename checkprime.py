num= int(input("Enter the number you want factors of: "))

# firstly to check whether the number is prime or not 
if (num>1):
    for i in range(2,num):
        if (num%i == 0):
            print(num,"is not prime")
						
# factors of the non-prime number            
            print(i, "times the" ,num//i ,"is", num)
            break
    else:
            print(num,"is prime, value must be a composite number")

# if number is less than 1, then no factors 
else:
    print(num,"is negative, value must be greater than 1")
