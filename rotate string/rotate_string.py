
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        listed_string = list(s)
        listed_goal = list(goal)

        for _ in range(len(listed_string)):
           if listed_string == listed_goal:
              return True
           else :
              shift_latter = listed_string.pop(0)
              listed_string.append(shift_latter)
        return False

s = "abcde"
goal = "bcgdea"



solution = Solution()


print(solution.rotateString(s, goal))



