
"""
Topic: Calculator
Samik Lalwani, 16010320038
Vallari Kulkarni, 16010320034
Atharva Kotkar, 16010320033

Problem Statement:
Write a program to create a calculator which can perform arithmetic 
operations like addition, subtraction, multiplication, division etc, 
depending upon input from the user. Create lists, functions, conditions 
and loops to execute the program.

"""
#%% Addition Function

def add():
    print("Enter numbers you want to add:")
    x = True
# Making sure numbers entered are int or float only..
    while x:
        try:
# Getting all the numbers in list format using map operator..
            l = list(map(float,input().split()))
            x = False
        except ValueError:
            print("Enter only integer or float value..")
            continue
                      
    n = len(l) 
    ans = 0
# Adding all the numbers in the list..
    for i in range(0,n):
        ans = ans + l[i]
    print("ANSWER IS:",ans)
 
#%% Subtraction Function

def subtract():
    print("Enter numbers you want to subtract:")
    x = True
# Making sure numbers entered are int or float only..
    while x:
        try:
# Getting all the numbers in list format using map operator..
            l = list(map(float,input().split()))
            x = False
        except ValueError:
            print("Enter only integer or float value..\n")
            continue
                      
    n = len(l) 
    l.sort()
# Finding the largest number in the list..
    sub = l[-1]
# Subtracting all the numbers in the list..
    for i in range(0,n-1):
        sub = sub - l[i]
    print("ANSWER IS\n",sub)

#%% Multiplication Function

def multiply():
    print("Enter numbers you want to multiply:")
    x = True
# Making sure numbers entered are int or float only..
    while x:
        try:
# Getting all the numbers in list format using map operator..
            l = list(map(float,input().split()))
            x = False
        except ValueError:
            print("Enter only integer or float value\n")
            continue
                  
    n = len(l)  
    mul = 1
# Multiplying all the numbers in the list..
    for i in range(0,n):
        mul = mul * l[i]
    print("ANSWER IS\n",mul)

#%% Divison Function  

def divide():
    x = True
# Making sure denominator is not zero..
    while x:
        try:
            val1=float(input("Enter 1st value:"))
            val2=float(input("Enter 2nd value:"))
# Using lambda operator to find division of 2 numbers..
            div = lambda a,b : a/b
            print("ASNWER IS:\n",div(val1,val2))
            x = False
        except ZeroDivisionError:
            print('\nYou cannot divide by zero !!\n')
            continue
            
            
#%%  Square root function  

def square_root():

    x = True
    while x:
        c=float(input("Enter value:"))
        if c > 0: 
# Using pow operator to find square root of number..
            root = pow(c,0.5)
            print("ANSWER IS:\n",root)
            x = False
        else:
            print("Please enter positive number only..")
            continue
           
    
#%% Exponential function  

def power():
    x = True
    while x:
        num = float(input("Enter number:"))    
        raise_to = float(input("Enter power:"))  
        if num > 0:
            answer = pow(num,raise_to)
            print("ANSWER IS:\n",answer)
            x = False
        elif num < 0:
            if raise_to > 1 or raise_to < -1:
                answer = pow(num,raise_to)
                print("ANSWER IS:\n",answer)
                x = False
            else: 
                print('Enter power greater than 1 or less than -1 only..')
                continue

#%% 

# Initiating infinite loop..
while True:
    print("Choose an operator:")
    operator=input("+ for addition, - for sub, * to multiply, / to divide, ^ for power, s for square root, e to exit:")

    if operator in ('+','-','*','/','^','s','e'):
        if operator == "+":
            add()
        elif operator == "-":
            subtract()
        elif operator == "*":
            multiply()
        elif operator == "/":  
            divide()
        elif operator == "^":
            power()
        elif operator == "s":
            square_root()
        elif operator == "e":
            break
    else:
        print("Error! Enter valid operator..")
        continue
    


    



    
    
    
    
    
    
    
    
    
    
    
    
    
    