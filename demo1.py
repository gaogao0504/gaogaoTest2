# 深拷贝和浅拷贝的区别
import copy

nums = [1, 2, 3]
nums1 = nums
# 没改变之前用的是同一个空间
print(nums1, nums)

# 浅拷贝
num2 = nums.copy()

# ward1是word的浅拷贝
words = ['hello', 'hogwatts',[ 'hurry', 'tom']]
# words1 = words.copy()
#
# words[0] = '哈罗'
# words[2][0] = 'hemin'
# 浅拷贝只拷贝第一层
# print(words1)
# print(words)


# 深拷贝,完全拷贝出一个新的内容
word2 = copy.deepcopy(words)
words[0] = '哈罗'
words[2][0] = 'hemin'
print(word2)
print(words)
