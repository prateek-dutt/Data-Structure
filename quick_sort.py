import numpy as np


def partition(x,lb,ub):
    a=x[lb]
    up=ub
    down=lb
    
    while down < up:
        while x[down] <= a and  down <ub:
            down +=1
        while x[up] >a:
            up-=1
        if down < up:
            ## interchange x[down] and x[up]
            
            temp=x[down]
            x[down]=x[up]
            x[up]=temp
            
    x[lb] = x[up]
    x[up] = a
    j=up
    return j
    
            
            




def quickSort(x,lb,ub):
    if lb >=ub:
        return ;
    
    # this is the partition function, the objective of partition function is to allow a speicific  elelement to find
    ## its proper position with respect to other elements in the subarray.  Refer Doc
    #
    #
    j=partition(x,lb,ub)
      
    quickSort(x,lb,j-1)
    quickSort(x,j+1,ub)
    

def main():
    arr=np.array([25,57,48,37,12,92,86,33])
    quickSort(arr,0,7)
    print(arr, end=" \n")
    


if __name__ == "__main__":
    main()