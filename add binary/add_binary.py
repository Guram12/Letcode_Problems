class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            sum = carry
            sum += int(a[i]) + int(b[i])
            print(sum)
            carry = sum // 2
            result.append(str(sum % 2))

        # Step 6: Handle final carry
        if carry != 0:
            result.append(str(carry))

        return ''.join(reversed(result))

soultion = Solution()

print(soultion.addBinary("10" , "1"))
