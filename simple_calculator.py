
def sum(num1,num2):
        return num1+num2

def sub(num1,num2):
        return num1-num2

def mult(num1,num2):
        return num1*num2

def div(num1,num2):
        return num1/num2

def mod(num1,num2):
        return num1%num2

flag= "1"
while(flag=="1"):
    num1=int(input ('enter number1: '))
    num2=int(input ('enter number2: '))

    symb=input("select operation ( +  ,  -  ,  *   ,  /  ,  % )")

    if(symb=="+"):
        print(sum(num1,num2))
    elif(symb=="-"):
        print(sub(num1,num2))
    elif(symb=="*"):
        print(mult(num1,num2))
    elif(symb=="/"):
        print(div(num1,num2))
    elif(symb=="%"):
        print(mod(num1,num2))
    
    flag= input('if you want to continue 1  , if you want to cancel 0')

    if flag=="0":
        break
    elif(flag !="0" and flag != "1" ):
        print("please enter valid input")


