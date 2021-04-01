# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or not k:
            return []
        if len(tinput) < k:
            return []
        heapq.heapify(tinput)
#         result = []
#         while k:
#             num = heapq.heappop(tinput)
#             result.append(num)
#             k -= 1
        return heapq.nsmallest(k, tinput)