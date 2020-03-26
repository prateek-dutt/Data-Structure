import sys
def selectionSort(array):
    for i in range(len(array)):
        min_indx=i
        for j in range(i+1,len(array)):
            if array[min_indx] > array[j]:
                min_indx=j
        array[i],array[min_indx]=array[min_indx],array[i]
def printArray(array):
    print("Sorted Array")
    for i in range(len(array)):
        print(array[i])

def main():
    print("SELECTION SORT ALGORITHM")
    len=input("Enter the size of your array")
    len=int(len)
    array=[]*len

    for i in range(len):
        val=input()
        array.append(val)
    selectionSort(array)
    printArray(array)

if __name__ == '__main__':
    main()




