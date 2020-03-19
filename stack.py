stack_size=100

class Stack:
    top=-1
    items=[]


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
    if stack.top == stack_size-1:

        return True
    else:
        stack.top=stack.top+1
        stack.items.insert(stack.top,x)
    return False



def push(stack,px):
    if push_and_test(stack,px):
        print("STACK OVERFLOW \n")

        index=input("\n Do you want to remove any element, please specify index number")

        pop(stack,index)
    else:
        print("Item has been inserted successfully")

def pop(stack,px):
    if pop_and_test(stack,px):
        print("STACK UNDERFLOW \n")
        print("To push an element please enter")
        num=input()
        push(stack,num)
    else:
        #Stack is not empty, green flag, we can pop the top element off
        print("ELEMENT POPPED")



def my_main():
    stack=Stack()
    # if empt(stack):
    #     print("Stack is Empty")
    i=0
    while(i<stack_size):
        num=input("Enter the items you want to insert into stack")
        push(stack,num)
        if i>=0:
            ans=input("Enter q to stop")
            if ans is "q":
                print("I want to quit")
                break;
            else:
                i+=1
        i+=1
    print("You can do anything with stack")

if __name__ == '__main__':
    my_main()