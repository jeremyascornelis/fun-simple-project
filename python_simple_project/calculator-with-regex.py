import re

print("Calculator with Python")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous) + " ")

    if equation == 'quit' :
        print('Goodbye, human!')
        run = False
    else:
        #anticipate the dangerous of eval()
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation) #only accept number

        if(previous == 0):
            previous = eval(equation)
        else:
            previous = eval(str(previous) + " " + equation)


while run:
    performMath()