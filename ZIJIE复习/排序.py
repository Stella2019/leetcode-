#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
class Solution:
    def MySort(self, arr):
        #         # write code here
        #         if not arr:
        #             return []
        #         def quicksort(arr, low, high):
        #             pivot = arr[low]
        #             if low>=high:
        #                 return None
        #             left = low
        #             right = high
        #             while left<right:
        #                 while left<right and arr[right]>pivot:
        #                     right-=1
        #                 while left<right and arr[left]<=pivot:
        #                     left+=1
        #                 arr[left], arr[right] = arr[right], arr[left]
        #             arr[low], arr[right] = arr[right], arr[low]
        #             quicksort(arr, low, right-1)
        #             quicksort(arr, right+1, high)

        #         quicksort(arr, 0 , len(arr)-1)
        #         return arr
        arr = sorted(arr)
        return arr