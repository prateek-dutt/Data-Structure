MAX_SIZE=100
MAX_COLS=80
class Stack:
    top=-1
    items=[]
def pop(stack):
    ##Considering stack is not empty
    #function should return the value of top of the stack after popping
    top = stack.top
    stack.top=stack.top-1
    return top
def push(stack,val):
    stack.top+=1
    stack.items.insert(stack.top,val)
    return stack.top
def oper(char,op1,op2):
    if char is '+':
        return(op1+op2)
    else:
        print("FUCK WORK IN PROGRESS")
def eval(expr):
    open_stack=Stack()
    for char in expr:
        if char>='0' and char<='9':
            print(char)
            push(open_stack,int(char))
        else:
            #character is an operator
            opnd2=pop(open_stack)
            opnd1=pop(open_stack)
            value=oper(char,opnd1,opnd2)
            push(open_stack,value)
    return (pop(open_stack))

def main():
    expr=[' ']
    expr=input("Enter the postfix expression")
    print("Original Postfix Expression",expr)
    print("Evaluated Result",eval(expr))
if __name__ == '__main__':
    main()
