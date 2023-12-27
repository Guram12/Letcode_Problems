from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        numbers = []
        for i , t in  enumerate(nums):
          if (t < target):
            numbers.append(nums[i])
            continue
          if t == target:
            return i
          else:
             return i 
        return(i + 1)

