from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      number_str = ''.join(map(str,digits))
      int_number = int(number_str) + 1
      number_str_2 = str(int_number)
      result = map(int , number_str_2)
      result2 = list(result)
      return (result2)

