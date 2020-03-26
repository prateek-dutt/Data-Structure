MAXSTACK=100

def quicksort(x,n):
    class bndtype:
        def __init__(self):
            self.lb=0
            self.ub=0
    
    
    newbnd= bndtype()
    
    
    #STACK 
    def empty(stack):
         if stack.top is -1:
             return True
         else:
             return False
    class Stack:
        def __init__(self):
            top=0
            bounds=[bndtype() for _ in range(MAXSTACK)]
            
    stack =  Stack()
    stack.top=-1
    newbnd.ub=n-1
    stack.push(newbnd)
    
    while empty(stack)!=True:
        popsub(stack,newbnd)
        while newbnd.ub > newbnd.lb:
            j=partition(x,newbnd.lb,newbnd.ub)
            if  j - newbnd.lb > newbnd.ub  - j :
                i = newbnd.ub
                newbnd.ub = j-1
                stack.push(newbnd)
                newbnd.lb = j+1
                newbnd.ub = i
            else:
                
    
    
            
            
    
              
          
              
