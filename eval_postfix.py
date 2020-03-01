
MAX_COLS=100
class Stack:
    top=-1
    items=[]*MAX_COLS
def empt(stack):
    if stack.top is -1:
        return True
    return False
def pop_and_test(stack,px):
    if empt(stack):
        return True
    pund=False

    px=stack.items[stack.top-1]
    stack.top = stack.top - 1

    return False

def push_and_test(stack,x):
    if stack.top ==MAX_COLS-1:

        return True
    else:
        stack.top=stack.top+1
        stack.items.insert(stack.top,x)
    return False
def oper(symb,op1,op2):


def pop(stack,px):
    if pop_and_test(stack,px):
        print("STACK UNDERFLOW \n")
        print("To push an element please enter")
        num=input()
        push(stack,num)
    else:
        #Stack is not empty, green flag, we can pop the top element off
        print("ELEMENT POPPED")

def push(stack,px):
    if push_and_test(stack,px):
        print("STACK OVERFLOW \n")

        index=input("\n Do you want to remove any element, please specify index number")

        pop(stack,index)
    else:
        print("Item has been inserted successfully")

def eval(expr):
    c,position=0
    opnd1,opend2,value=00.00
    open_stack=Stack()
    open_stack.top=-1
    for char in expr:
        if char is int:
            push(open_stack,char)
        else:
            opnd2=pop(open_stack)
            opnd1=pop(open_stack)
            value=oper(char,opnd1,opnd2)
            push(open_stack,value)
    return(pop(open_stack))






def main():
    expr=['']*MAX_COLS
    position=0
    eval()
    while char in expr:
        print(expr+"original postfix expression")
        
    print(eval(expr))
    

