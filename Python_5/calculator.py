import os
def add(n1 , n2):
    return n1 + n2 
def sub (n1 , n2):
    return n1 - n2
def multi(n1 , n2):
    return n1 * n2 
def div (n1 , n2):
    return n1 / n2

opration = {

    "+" : add ,
    "-" :sub ,
    "*" :multi,
    "/" :div
}
def calculator():
    num1 = float(input(" Insert the first number : "))
    for symbol in opration:
        print(symbol)
    direction = True
    while direction is True:
        choose_opration = input("Choose the opration please : ")
        num2 = float(input(" Insert the second number : "))
        calcu_function = opration[choose_opration]    
        answer = calcu_function(num1 , num2)
        print(answer)
        if input(f"type 'y' to continue calculating with {answer} or type 'n' to calculating new : ") == 'y':
            num1 = answer
        else:
            direction = False
            os.system('cls')
            calculator()
calculator()    