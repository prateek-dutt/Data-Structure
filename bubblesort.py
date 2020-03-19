import numpy as np
def bubble(x,n):
    
    hold=pss=0
    switched=True
    
    while pss < n-1 and switched is True:
        switched=False
        
        for j in range(n-pss-1):
            if x[j] > x[j+1]:
                switched=True 
                hold=x[j]
                x[j]=x[j+1]
                x[j+1]=hold
                
           
        pss+=1


def main():
    arr=np.array([12,11,4,5,1])
    print(arr)
    bubble(arr,5)
    print(arr)
    

if __name__ == '__main__':
    main()
    
            
            
    