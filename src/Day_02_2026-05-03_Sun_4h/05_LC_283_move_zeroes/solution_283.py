# LC 283 — Move Zeroes
def moveZeroes(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)) :
      if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i] 
        j += 1

if __name__ == "__main__":
    arr1 = [0,1,0,3,12]
    moveZeroes(arr1)
    print(arr1)  # Output: [1, 3, 12, 0, 0]

    arr2 = [0]
    moveZeroes(arr2)
    print(arr2)  # Output: [0]

    arr3 = [1, 0, 2, 0, 3]
    moveZeroes(arr3)
    print(arr3)  # Output: [1, 2, 3, 0, 0]   
        