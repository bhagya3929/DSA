class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 1 % k
        for length in range(1, k + 1):
            # Check if current repunit is divisible by k
            if remainder == 0:
                return length
            remainder = (remainder * 10 + 1) % k
        return -1