class BinHeap:
    def __init__(self, max_size):
        self.heapList = [0]
        self.currentSize = 0
        self.max_size = max_size

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        while self.size() > self.max_size:
            self.delMin()
        if self.size() < self.max_size:
            self.heapList.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)
        elif self.size() == self.max_size:
            if k <= self.findMin():
                pass
            else:
                self.delMin()
                self.heapList.append(k)
                self.currentSize = self.currentSize + 1
                self.percUp(self.currentSize)
        self.heapList.sort()

    def findMin(self):
        return self.heapList[1]

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
       
        if self.size() <= self.max_size:
            i = len(alist) // 2
            self.currentSize = len(alist)
            self.heapList = [0] + alist[:]
            while (i > 0):
                self.percDown(i)
                i = i - 1
            while self.size() > self.max_size:
                self.delMin()
        self.heapList.sort()


    def size(self):
        return self.currentSize

    def isEmpty(self):
        return self.currentSize == 0

    def __str__(self):
        txt = "{}".format(self.heapList[1:])
        return txt


if __name__ == '__main__':
    bh = BinHeap(5)
    bh.buildHeap([9, 5, 6, 2,7,20,11,4])
    bh.insert(7)
    bh.insert(19)
    print(bh)
