'''
Welcome to my math calculator, I tried to make it as my first project:)
'''
def mathtest():
    #The grettings
    print("Welcome to the math calculator")
    while True:
        try:
            x = float(input("Enter your first number: "))
            break
        except ValueError:
            print("Only integers or decimals allowed!")

    while True:
        try:
            y = float(input("Enter your second number: "))
            break
        except ValueError:
            print("Only integers or decimals allowed!")

    #The options to do the math
    while True:
        z = input("Enter yopur desired operators: ADD, SUBTRACT, MULTIPLY, DIVIDE: ")
        
        try:
            if not isinstance(z, str):
                raise Typeerror ("Only text allowed!")
        except TypeError as e:
            print(f"Error: {e}")
        
        if z == "ADD":
            result = x + y
            print(result)
            break 
        elif z == "SUBTRACT":
            result = x - y
            print(result)
            break
        elif z == "MULTIPLY":
            result = x * y
            print(result)
            break
        elif z == "DIVIDE":
            result = x / y
            print(result)
            break
        else:
            print("Choose only from the options!")
        
if __name__ == "__main__":
    mathtest()