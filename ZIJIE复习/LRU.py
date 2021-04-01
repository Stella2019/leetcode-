#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组

import collections
import sys


class Solution:
    def __init__(self, k):
        self.dic = collections.OrderedDict()
        self.capacity = k

    def set(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dic.popitem(False)
        self.dic[key] = value

    def get(self, key):
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val
        return val


for line in sys.stdin.readlines():
    line = line.strip()
    line = line.replace(' ', '')
    a = line.split(']],')
    k = int(a[1])
    res = []
    s = Solution(k)
    for item in a[0][2:].split('],['):
        m = item.split(',')
        if m[0] == '1':
            s.set(int(m[1]), int(m[2]))
        else:
            res.append(s.get(int(m[1])))
    print(str(res).replace(' ', ''))

import sys


class Solution:
    l, d = [], {}
    length = 0
    k = 0
    out = []

    def __init__(self, k):
        self.k = k

    def LRU(self, operators, k):
        self.k = k
        for o in operators:
            if o[0] == 1:
                self.set(o[1], o[2])
            elif o[0] == 2:
                self.out.append(self.get(o[1]))
        # write code here
        return self.out

    def get(self, key):
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
            return self.d[key]
        return -1

    def set(self, key, value):
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
        else:
            self.l.append(key)
            self.d[key] = value
        if len(self.l) > self.k:
            old = self.l.pop(0)
            self.d.pop(old)


for line in sys.stdin.readlines():
    line = line.strip()
    line = line.replace(' ', '')
    a = line.split(']],')
    k = int(a[1])
    res = []
    s = Solution(k)
    for item in a[0][2:].split('],['):
        m = item.split(',')
        if m[0] == '1':
            s.set(int(m[1]), int(m[2]))
        else:
            res.append(s.get(int(m[1])))
    print(str(res).replace(' ', ''))