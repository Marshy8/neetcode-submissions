class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = False
        added = False
        count = 0

        while (carry or added is False) and count < len(digits):
            if digits[count] == 9:
                digits[count] = 0
                count += 1
                carry = True
            else:
                digits[count] += 1
                added = True
                carry = False

        if not added:
            digits.append(1)
        digits.reverse()
        return digits