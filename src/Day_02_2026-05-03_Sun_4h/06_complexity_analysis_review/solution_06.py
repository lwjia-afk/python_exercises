### 1. Two nested loops over `nums` of size n
from collections import defaultdict


def twoSumNestedLoops_withDuplicate(nums: list[int], target: int) -> list[list]:
    numSet = defaultdict(list)
    res = []
    for i, num in enumerate(nums):
        numSet[num].append(i)

    for num in numSet.keys():
        com = target - num
        if com in numSet:
            if com == num:
                if len(numSet[num]) > 1:
                    res.append([num, num])
            else:
                res.append([num, com])
    return res


def twoSumNestedLoops_withoutDuplicate(nums: list[int], target: int) -> list[list]:
    numSet = defaultdict(list)
    res = []
    for i, num in enumerate(nums):
        numSet[num].append(i)

    for num in numSet.keys():
        com = target - num
        if com in numSet:
            if com == num:
                if len(numSet[num]) > 1:
                    res.append([num, num])
            else:
                if num < com:  # To avoid duplicates like [2, 7] and [7, 2]
                    res.append([num, com])
    return res

### 2. Iterating once and using a `set` for membership
def twoSumSet(nums: list[int], target: int) -> list[list]:
    seen = set()
    res = []
    for num in nums:
        complement = target - num
        if complement in seen:
            res.append([complement, num])
        seen.add(num)
    return res

### 3. Sorting `nums` then doing one pass
def countUnique(nums: list[int]) -> int:
    if not nums : return 0
    nums.sort()
    
    current = nums[0]
    count = 1
    for num in nums : 
        if num != current:
            count += 1
            current = num 
    return count
    


if __name__ == "__main__":
    print(twoSumNestedLoops_withDuplicate([2, 7, 11, 15], 9))  # Output: [[2, 7]]
    print(twoSumNestedLoops_withDuplicate([3, 2, 4], 6))       # Output: [[2, 4]]
    print(twoSumNestedLoops_withDuplicate([3, 3, 3], 6))          # Output: [[3, 3]]
    print(twoSumNestedLoops_withoutDuplicate([2, 7, 11, 15], 9))  # Output: [[2, 7]]
    print(twoSumNestedLoops_withoutDuplicate([3, 2, 4], 6))       # Output: [[2, 4]]
    print(twoSumNestedLoops_withoutDuplicate([3, 3, 3], 6))          # Output: [[3, 3]]
    print(twoSumSet([2, 7, 11, 15], 9))  # Output: [[2, 7]]
    print(twoSumSet([3, 2, 4], 6))       # Output: [[2, 4]]
    print(twoSumSet([3, 3, 3], 6))          # Output: [[3, 3]]
    print(countUnique([1, 2, 2, 3, 4, 4, 4, 5]))  # Output: 5   