import time


class BinHeap:
    """
    The lecture HEAP
    """
    def __init__(self):
        """
        self.heapList: list of elements
        self.currentSize: Size(length) of the list
        """
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        """
        Function that moves up elements to keep order in heap
        :param i: index od element
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        """
        Function that adds element to the heap
        :param k: element
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def findMin(self):
        """
        Function that searches the smallest element
        :return: The smallest element
        """
        return self.heapList[1]

    def percDown(self, i):
        """
        Function that moves down elements to keep order in heap
        :param i: index od element
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        """
        Function that searches the index of the smallest child
        :param i: the index from which we start our search
        :return: index of the smallest child
        """
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        """
        Function that removes the smallest element and keeps heap in order
        :return: the smallest element
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        """
        Function that creates heap from the list
        :param alist: list that will become a heap
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def size(self):
        """
        Function that checks the size(length) of the heap
        :return: size of the heap
        """
        return self.currentSize

    def isEmpty(self):
        """
        Function that checks if the heap is empty
        :return: True or False
        """
        return self.currentSize == 0

    def __str__(self):
        """
        Function that shows the heap
        :return: heap
        """
        txt = "{}".format(self.heapList[1:])
        return txt


def sorting(list1):
    """
    Function that sorts elements in the heap
    :param list1: list that will become the heap
    :return: sorted list and the time of function work
    """
    start = time.time()
    heap = BinHeap()
    heap.buildHeap(list1)
    list2 = []
    for element in range(0, len(list1)):
        list2.append(heap.findMin())
        heap.delMin()
    end = time.time()
    alg_time = end - start
    return list2, alg_time


if __name__ == '__main__':
    print(sorting([1, 4, 5, 8, 3, 2, 7, 4, 5, 3]))


