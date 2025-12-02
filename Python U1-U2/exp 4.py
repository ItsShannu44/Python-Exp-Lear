from collections import OrderedDict

n = int(input("Enter the num of integers: "))
nums = list(map(int, input().split()))

od = OrderedDict.fromkeys(nums)
print("The first occurences of ordered dictonary: "*od)
