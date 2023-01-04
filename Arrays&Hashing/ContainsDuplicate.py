# Given an array nums, return true if any value appears at least twice in the array , and return false if every element is distinct

# Brute Force 

# Time: O(n^2)

# Space: O(1)

def containsDuplicate(nums):
    hashSet = set()

    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False 
