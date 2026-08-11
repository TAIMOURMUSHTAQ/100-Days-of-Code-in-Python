import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
#Adding these 4 functions in a dictionary as the values
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#Use the dict operation to perform calculation
# print(operations["*"](4,8))
def calculator(): #we can use another while loop instead of this recursive function
    should_accumulate = True
    num1=float(input("What is the first number?:  "))
    while should_accumulate:
        # print("+\n-\n*\n/")
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What is the next number?:  "))
        answer=operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice=input(f"Type 'y' to continue calculating with {answer},type 'n' to start a new calculation or anything else to exit.  ").lower()
        if choice=="y":
            num1=answer
        elif choice=="n":
            should_accumulate=False
            print("\n"*20)
            calculator()
        else:
            print(f"You chose {choice}.Good Bye!")
calculator()