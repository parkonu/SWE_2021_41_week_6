from typing import List
str = input("Input: nums = ")
target = int(input("target = "))
nums = list(map(int, str.strip('[]').split(',')))

def addTwoNum(num: List[int], target: int) -> List[int]:
    pair = {}
    for index, num in enumerate(num):
        if num in pair:
            return [pair[num], index]
        pair[target - num] = index


result = addTwoNum(nums, target)
print(f"Output: {result}")