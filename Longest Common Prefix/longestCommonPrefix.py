from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if not strs:
          return ""

      # Find the shortest string in strs
      shortest_str = min(strs, key=len)

      # Iterate through each character in the shortest string
      for i, char in enumerate(shortest_str):
          for other in strs:
              # Compare the character with the same position in other strings
              if other[i] != char:
                  # If not matching, return the common prefix up to this point
                  return shortest_str[:i]

      return shortest_str  # The entire shortest string is the common prefix

