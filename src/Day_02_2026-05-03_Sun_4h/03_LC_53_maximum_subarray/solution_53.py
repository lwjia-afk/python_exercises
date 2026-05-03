# LC 53 — Maximum Subarray
def maxSubArray(nums: list[int]) -> int:
    if not nums:
        return 0
    
    current = best = nums[0]
    for num in nums:
        current = max(num, current + num)
        best = max(best, current)
    return best
    
if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(maxSubArray([1]))                       # Output: 1
    print(maxSubArray([5,4,-1,7,8]))             # Output: 23