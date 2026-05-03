###Given an integer array `nums`, return `True` if any value appears at least twice, else `False`.

def containsDuplicateWithSet(nums: list) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def containsDuplicateWithLen(nums: list) -> bool:
    return len(set(nums)) < len(nums)



if __name__ == "__main__":
    print(containsDuplicateWithSet([1, 2, 3, 1]))  # True
    print(containsDuplicateWithSet([1, 2, 3, 4]))  # False
    print(containsDuplicateWithSet([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
    print(containsDuplicateWithLen([1, 2, 3, 1]))  # True
    print(containsDuplicateWithLen([1, 2, 3, 4]))
