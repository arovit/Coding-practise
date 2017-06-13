#!/usr/bin/python
expression = "1*2+2*4+2+4*3-1"

Priority = {
'*':2,
'/':2,
'+':1,
'-':1
}

def perform(operator, arg1, arg2):
    if operator == "/":
        return int(arg1) / int(arg2)
    elif operator == "*":
        return int(arg1) * int(arg2)
    elif operator == "+":
        return int(arg1) + int(arg2)
    elif operator == "-":
        return int(arg1) - int(arg2)

def isOperand(token):
    return token not in Priority.keys() 

def process_expression(expression):
    operatorStack = []
    operandStack = []
    for i in expression:
        if isOperand(i):
            operandStack.append(i) 
        else:  # operator
            process_operations(i, operatorStack, operandStack)
    return end_processing(operatorStack, operandStack)
            
def end_processing(operatorStack, operandStack):
    end_result = 0 
    while operatorStack:
        op = operatorStack.pop()
        arg2 = operandStack.pop()
        arg1 = operandStack.pop()
        end_result = perform(op, arg1, arg2)
        operandStack.append(end_result)
    return operandStack[-1]
        
def process_operations(i, operatorStack, operandStack):
    if not operatorStack:
        operatorStack.append(i) 
        return
    tos = operatorStack[-1]
    if Priority[tos] < Priority[i]:
        operatorStack.append(i) 
    else:
        operator = operatorStack.pop()
        arg2 = operandStack.pop()
        arg1 = operandStack.pop()
        result = perform(operator, arg1, arg2)
        operandStack.append(result)
        process_operations(i, operatorStack, operandStack)

print process_expression(expression)
