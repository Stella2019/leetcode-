有一个整数数组，请你根据快速排序的思路，找出数组中第K大的数。

给定一个整数数组a,同时给定它的大小n和要找的K(K在1到n之间)，请返回第K大的数，保证答案存在。

这题应该是用快排的思想：例如找49个元素里面第24大的元素，那么按如下步骤：

1.进行一次快排（将大的元素放在前半段，小的元素放在后半段）,假设得到的中轴为p

2.判断 p - low + 1 == k ，如果成立，直接输出a[p]，（因为前半段有k -
1个大于a[p]的元素，故a[p]为第K大的元素）

3.如果 p - low + 1 > k， 则第k大的元素在前半段，此时更新high = p - 1，继续进行步骤1

4.如果p - low + 1 <  k， 则第k大的元素在后半段， 此时更新low = p + 1, 且 k = k -
(p - low + 1)，继续步骤1.

由于常规快排要得到整体有序的数组，而此方法每次可以去掉“一半”的元素，故实际的复杂度不是o(nlgn), 而是o(n)。

def findKth(a, left, right, k):
    # write code here
    low = left
    high = right
    key = a[left]
    while left < right:
        while left < right and a[right] <= key:
            right -= 1
        a[left] = a[right]
        while left < right and a[left] >= key:
            left += 1
        a[right] = a[left]
    a[left] = key
    if (left == k - 1):
        return a[left]
    elif (left > k - 1):
        return findKth(a, low, left - 1, k)
    else:
        return findKth(a, left + 1, high, k)


import sys

try:
    while (True):
        line = sys.stdin.readline()
        if line == '':
            break
        lines = line.strip().replace('[', '').replace(']', '').split(',')
        lines = list(map(int, lines))
        size = lines[-2]
        k = lines[-1]
        ret = findKth(lines, 0, size - 1, k)
        print(ret)
except:
    pass


def quickselect(array, k):
    position = k - 1
    return quickselectHelper(array, 0, len(array) - 1, position)


def quickselectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]





# -*- coding:utf-8 -*-


def findKth( a, left,right, k):
        # write code here
        low=left
        high=right
        key=a[left]
        while left<right:
            while left<right and a[right]<=key:
                  right-=1
            a[left]=a[right]
            while left<right and a[left]>=key:
                left+=1
            a[right]=a[left]
        a[left]=key
        if(left==k-1):
            return a[left]
        elif(left>k-1):
            return findKth(a,low,left-1,k)
        else:
            return findKth(a,left+1,high,k)
import sys
try:
    while(True):
        line=sys.stdin.readline()
        if line=='':
            break
        lines=line.strip().replace('[','').replace(']','').split(',')
        lines=list(map(int,lines))
        size=lines[-2]
        k=lines[-1]
        lines = lines[:-2]
        ret=findKth(lines, 0, size-1, k)
        print(ret)
except:
    pass



#class Solution:
    #def findKth(self, a, n, K):
        # write code here

while True:
    try:
        x=input().replace(']', '')
        x=x.replace('[', '')
        x=list(x.split(','))
        k=int(x.pop())
        n=int(x.pop())
        tmp=list(map(int,x))
        tmp.sort(reverse=True)
        print(tmp[k-1])
    except:break