'''
Welcome to my math calculator, I tried to make it as my first project :)
This is the improved version!
'''
def greet():
    print('-'*40)
    print("Welcome to the math calculator, my first project ever!")
    print("I'd appreciate if you try this calculator by yourself.")
    print('-'*40)

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number:     "))
            num2 = float(input("Enter the second number:    "))
            return num1, num2
        except ValueError:
            print("Please type only integers or decimals")

def get_operator():
    operator = ['+', '-', '*', '/', 'add', 'subtract', 'multiply', 'divide']
    while True:
        op = input('Enter operator (+, -, *, /) or (add, subtract, multiply, divide):    ').lower()
        if op in operator:
            return op
        print('Please choose from the options given!')

def calculate(num1, num2, op):
    if op == '+' or op == 'add':
        return num1 + num2
    elif op == '-' or op == 'subtract':
        return num1 - num2
    elif op == '*' or op == 'multiply':
        return num1 * num2
    elif op == '/' or op == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            print('Cannot divide a number by zero!') 

def main():
    greet()
    
    while True:
        num1, num2 = get_numbers()
        op = get_operator()
        result = calculate(num1, num2, op)
        
        if result is not None:
            print('-'*40)
            print(f"Result: {num1} {op} {num2} = {result}")
            print('-'*40)

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print('-'*40)
            print("Thanks for using my calculator, have a nice day!")
            print('-'*40)
            break

if __name__ == "__main__":
    main()
    main()
