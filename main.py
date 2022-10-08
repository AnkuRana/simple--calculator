#calculator
from art import logo
print(logo)
#addition
def add (n1,n2):
    return n1 + n2

#subtract
def subtract(n1,n2):
    return n1 - n2

#Mulitply
def multiply(n1,n2):
    return n1 * n2

#divide
def divide(n1,n2):
    return n1 / n2

opeartions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    
    is_continue =True
    
    num1 = float(input("enter the first number: "))
    print("Choose one of the following operations...")
        
    for key in opeartions:
            print(key)
        
    while is_continue:
        num2 = float(input("enter the next number: "))
        select_operation = input("Chosen Opeartion: ")
        function = opeartions[select_operation]
        value = function(num1,num2)
        print(f"\n {num1} {select_operation} {num2} = {value}")
        option_cont = input("Type 'Y' you want to contine calculaions! OR 'N' if u want to start fresh calculations OR type anything else to exit calculator: ").lower()
        if option_cont == "n":
            is_continue = False
            calculator()
        elif option_cont == "y":
            num1 = value
        else:
            print("**** Exit ***")
            is_continue = False

calculator()
    
    
    
        
        