# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。##给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
"""
def binarySearch(nums, target);
    return binarySeachHelper(nums, target, 0, len(nums) -1 )

def binarySearchHelper(nums, target, left, right):
    if left > right:
        return -1
    middle = (left + right)//2
    potentialMatch =  nums[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(nums, target, left, middle - 1)
     else:
         return binarySearchHelper(nums, target, middle + 1, right)

"""

l, r = 0, len(nums) - 1
ans1 = -1
while l <= r:
    mid = l + (r - l) // 2
    if nums[mid] == target:
        ans1 = mid
        r = mid - 1
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
if ans1 == -1:
    print(-1, -1)
else:
    ans2 = -1
    l, r = ans1, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            ans2 = mid
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
print(ans1, ans2)

无序数组求中位数
Class
MedianFinder:


def _init_(self):
    self.store = []


def addNum(self, num):
    if not self.store:
        self.store.append(num)

else:
bisect.insort_left(self.store, num)


def findMedian(self):
    n = len(self.store)
    if n & 1 == 1:
        return self.store[n // 2]


def quicksort(num):




