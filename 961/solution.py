class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_of_repeats = len(nums) // 2
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if counts[num] == num_of_repeats:
                return num
