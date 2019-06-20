# 11. 如何高效的找出一个字符串中最长重复次数的字符串，并计算其重复次数
# 'abc fghi bc kl abcd lkm abcdefg'
# 答案为：abcd 2

char = 'abc fghi bc kl abcd lkm abcdefg'
char_list = char.split(' ')  # 分割字符串，生成列表
repeat_list = []
for item in char_list:  # 迭代字符串列表，计算重复次数，将重复次数大于1的加入重复列表
    char_dict = {'char': item, 'len': len(item), 'count': char.count(item)}
    if char_dict['count'] > 1:
        repeat_list.append(char_dict)
result = max(repeat_list, key=lambda x: x['len'])  # 获取字符最大的字典
print(result['char'], result['count'])


# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        # 字典样式：{数字：索引}，如{2：0，3：1，5：2}
        for index, num in enumerate(nums):
            anothernum = target - num  # 另外一个数字的值
            if anothernum in hashmap:  # 如果另外一个值在字典中
                return [hashmap[anothernum], index]  # 返回另一个值和当前值的索引
            elif hashmap.get(num) is None:  # 如果hashmap里面不存在，添加内容
                hashmap[num] = index
            continue


nums = [2, 7, 2, 9]
target = 11
solu = Solution()
res = solu.twoSum(nums, target)
print(res)
