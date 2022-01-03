import collections

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    """def Check(self):
        counter = 0
        tree = self.key, self.leftChild, self.rightChild
        for keys in tree:
            dup = [item for item, count in collections.Counter(tree).items() if count > 1]
        tree.pop(dup)"""


if __name__ == '__main__':
    r = BinaryTree('a')
    print("Root key = ", r.getRootVal())
    print("Left child = ", r.getLeftChild())
    r.insertLeft('b')
    print("Left child after insertion (reference) = ", r.getLeftChild())
    print("Left child after insertion (value) = ", r.getLeftChild().getRootVal())
    r.insertRight('c')
    print("Right child after insertion (reference) = ", r.getRightChild())
    print("Right child after insertion (value) = ", r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('Keri')
    print("Root key after update = ", r.getRightChild().getRootVal())
    #print(r.Check())
