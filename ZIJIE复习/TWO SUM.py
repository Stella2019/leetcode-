class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        res = [0,0]#保存结果
        mp = {}#定义一个哈希表存储numbers[i]和对应的下标
        for i in range(len(numbers)):#进行标记
            mp[numbers[i]] = i
        for i in range(len(numbers)):
             #每遍历一个numbers[i]就去对应的mp里找有没有target - numbers[i]
             #如果有就返回结果
             #如果没有就找下一个
            if target - numbers[i] in mp:
                if mp[target - numbers[i]] != i:
                    res[0] = i + 1
                    res[1] = mp[target - numbers[i]]
                    return res
        return res


#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers, target):
        res = []
        dic = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in dic:
                return [dic[tmp] + 1, i + 1]
            dic[numbers[i]] = i


while True:
    try:
        import sys

        s = Solution()
        lines = str(sys.stdin.readline().strip())
        target = int(lines.split(',')[-1])
        numbers = list(map(int, lines.split(']')[0].split('[')[-1].split(',')))
        res = s.twoSum(numbers, target)
        print('[%d,%d]' % (res[0], res[1]))
    except:
        break
        # write code here