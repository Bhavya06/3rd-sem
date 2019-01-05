def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x//y

print("Choose the operation needed to perform")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
i = int(input("Enter option number"))

a = int(input("enter first number"))
b = int(input("enter second number"))

if(i==1):
    print("The sum is ",add(a,b))
elif(i==2):
    print("The difference is ",sub(a,b))
elif(i==3):
    print("The product is ",mul(a,b))
elif(i==4):
    print("The quotient is ",div(a,b))
else:
    print("Please enter a valid option")