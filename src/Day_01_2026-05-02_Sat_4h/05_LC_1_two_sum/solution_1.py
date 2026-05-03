def twoSum(nums: list[int], target: int) -> list[int]:
    sorted_nums = list(enumerate(nums))
    sorted_nums.sort(key=lambda x: x[1])

    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        if current_sum == target:
            return [sorted_nums[left][0], sorted_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

def twoSumSet(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(twoSum([3, 3], 6))          # Output: [0, 1]
