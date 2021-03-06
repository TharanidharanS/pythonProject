#1. Write a Python program to find three numbers from an array such that the sum of three numbers equal to a given number
def three_Sum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            sum = target - nums[i] - nums[j]
            left, right = j + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == sum:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > sum:
                    right -= 1
                else:
                    left += 1
    return result
print(three_Sum([1, 5, -1, -5], 0))

#2.Write a Python program to compute and return the square root of a given 'integer'
import math
input = int(input("enter the number:"))
sq = math.sqrt(input)
print(f"square root of {input} is:",sq)


