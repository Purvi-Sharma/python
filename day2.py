#even -odd display
num1=int(input("enter a no."))
if num1%2==0:
    print("no. is even")
else:
    print("no.is odd")  
#check whether no. is positive/negative/zero   
if num1>0:
    print("no.is positive")
elif num1==0:
    print("no. is zero")
else:
    print("no. is negative")       
#largest of three no.           
num2=int(input("enter another no."))
num3=int(input("another one"))
if num1==num2==num3:
    print("all are equal")
if num1==num2:
    if num1>num3:
        print("num1 and num2 are equal and are largest")
    else:
        print("num3 is largest")
if num2==num3:
    if num2>num1:
        print("num2 and num3 are equal and are largest")
    else:
        print("num1 is largest")
if num1==num3:
    if num1>num2:
        print("num1 and num 3 are equal and are largest")
    else:
        print("num2 is largest")   
if num1!=num2 and num2!=num3 and num1!=num3:
    if num1>num2 and num1>num3:
        print("num1 is greater")
    elif num2>num1 and num2>num3:
        print("num2 is greater ") 
    else:
        print("num3 is greater")       


