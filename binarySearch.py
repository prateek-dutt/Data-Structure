###NEVER BE ASHAMED OF YOUR STUPIDITY,BEAWARE OF ARROGANCE OF KNOWLEDGE



###This is the non recursive version

class binarySeach():
    def __init__(self,arr,key,size):
        self.arr = arr
        self.key = key 
        self.size = size
        print(self.run(self.arr, self.key,self.size))
    def run(self,arr,key,size):
        low=0
        high =size-1
        while low <= high:
            mid = int((low + high) /2)
            if key == arr[mid]:
                return (mid)
            if key < arr[mid]:
                high = mid - 1
            else:
                low = mid +1
        return -1
  
class RecBinSr():

    def recSearch(self,arr,key,low,high):
      
        
        if low  > high :
            return(-1)
        mid =int((low + high) /2)
        if key is self.arr[mid]:
            return(mid)
        elif key < self.arr[mid]:
            self.recSearch(arr,key,low,mid-1)
        else:
            self.recSearch(arr,key,mid+1,high)
    def __init__(self,arr,key,size):
        self.arr = arr
        self.key = key
        self.size=size
        print(self.recSearch(self.arr,self.key,0,self.size))
  
  
  
  
  
def main():
    binSr=binarySeach([1,2,3,4],3,4) ## For NonRecursion
    bin = RecBinSr([1,2,3,4],3,4)
    

    
    
    
  
  
if __name__ == '__main__':
    main()
    