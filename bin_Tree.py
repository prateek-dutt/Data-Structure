import sys

class Node:
    def __init__(self):
        self.info=0
        self.left=None
        self.right=None

def pretrav(tree):
    if tree is not None:
        print(tree.info)
        pretrav(tree.left)
        pretrav(tree.right)
def posttrav(tree):
    if tree is not None:
        posttrav(tree.left)
        posttrav(tree.right)
        print("Posttrav",tree.info)
def intrav(tree):
    if tree is not None:
        intrav(tree.left)
        print(tree.info)
        intrav(tree.right)
def setleft(tree,x):

    if tree.left is not None:
        setleft(tree.left,None)
    else:
        tree.left=maketree(x)
def setright(tree,x):

    if tree.right is not None:
        setright(tree.right,x)
    else:
        tree.right=maketree(x)
def maketree(x):
    node=Node()
    node.info=x
    node.left=None
    node.right=None
    return node

def main():
    root=int(input("Enter the root"))
    bTree=maketree(root)
    number=input().split()
    print(number)

    for i in range(len(number)):
        number[i]=int(number[i])
        if int(number[i]) is bTree.info:
            print("This is a duplicate number")
        elif int(number[i]) < bTree.info:
            setleft(bTree,number[i])
        else:
            setright(bTree,number[i])
    pretrav(bTree)
if __name__ == '__main__':
    main()