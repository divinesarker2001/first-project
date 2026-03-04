'''
Welcome to my math calculator, I tried to make it as my first project :)
'''
def mathtest():
    #outer loop, for 'again' var
    while True: 
        # greetings to the user
        print('-'*40)
        print("Welcome to the math calculator, my first project ever!")
        print("I'd appreciate if you try this calculator by yourself.")
        print('-'*40)
        
        #user input 1 checker
        while True:
            try:
                x = float(input("Enter your first number: "))
                break
            except ValueError:
                print("Only integers or decimals allowed!")

        #user input 2 checker
        while True:
            try:
                y = float(input("Enter your second number: "))
                break
            except ValueError:
                print("Only integers or decimals allowed!")
        
        #operator loop
        while True:
            z = input("Enter operator (ADD, SUBTRACT, MULTIPLY, DIVIDE): ").upper()
            
            if z == "ADD":
                result = x + y
                result1 = '+'
            elif z == "SUBTRACT":
                result = x - y
                result1 = '-'
            elif z == "MULTIPLY":
                result = x * y
                result1 = '*'
            elif z == "DIVIDE":
                if y == 0:
                    print("Cannot divide by zero!")
                    continue  #stay in operator loop
                result = x / y
                result1 = '/'
            else:
                print("Choose only from the options!")
                continue  #stay in operator loop
            
            print(f"{x} {result1} {y} = {result}")
            break  #exit operator loop
        
        #the piece of code to ask wether you want to use the calculator agin
        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the calculator!")
            break  #exit outer loop
        
if __name__ == "__main__":
    mathtest()
