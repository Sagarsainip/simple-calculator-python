def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y
    

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select Operation")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice = input("Enter Your Choice (1/2/3/4/5): ")
 
        if choice == '5':
            print("Exit the calculator. Good Bye!")
            break
        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid Input. Please enter numeric values.")
                continue
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1,num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1,num2)}")
            else:
                print("Invalid Choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()                             