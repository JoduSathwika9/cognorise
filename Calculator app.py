def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error:Division by Zero"

while True:
    
    num1 = float(input("Enter first number: "))
    operation=input("Enter operation(+,-,*,/):")
    num2 = float(input("Enter second number: "))
    
    if operation=="+":
        result=add(num1,num2)
    elif operation=="-":
         result=subtract(num1,num2)
    elif operation=="*":
         result=multiply(num1,num2)
    elif operation=="/":
         result=divide(num1,num2)
    else:
        print("Invalid operation.please enter +,-,*,/.")
        continue
    
    print(f"Result:{result}")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation !='yes':
        break
        
        
