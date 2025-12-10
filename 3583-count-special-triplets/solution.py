class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        value_indexes = self.buildValueIndexDict(nums)

        special_triplet_count = self.findSpecialTriplets(value_indexes)

        mod = 10**9 + 7
        return special_triplet_count % mod

    def findSpecialTriplets(self, data) -> int:
        # sort keys ascending
        keys = sorted(data.keys())
        max_num = keys[-1]

        # iterate through keys finding suitable nums
        set_count = 0
        for num in keys:
            indexes = data[num]

            # check number index is not more than the max known
            desired_num = num*2
            if (desired_num > max_num):
                break

            # check a compatible list exists, has to exist or have more than one option
            i_k_indexes = data.get(desired_num)
            if i_k_indexes is None:
                continue
            i_k_indexes_len = len(i_k_indexes)
            if len(i_k_indexes) < 2:
                continue

            # loop through each j index, trying to find matching pairs
            prev_left = 0
            j_is_here = desired_num == num
            for j in indexes:
                # binary search to find left and right bound indexes
                left, right = self.findLeftRight(i_k_indexes, j, prev_left)
            
                # run left right checks to continue or cancel early
                if left == 0:
                    continue
                if right >= i_k_indexes_len:
                    break

                set_count += (left - (1 if j_is_here else 0)) * (i_k_indexes_len - right)
                prev_left = left

        return set_count

                
    def findLeftRight(self, data, value, prev_left):
        left, right =  prev_left, len(data)

        while left < right:
            mid = (left+right) // 2
            if data[mid] < value:
                left = mid + 1
            else:
                right = mid

        return left, left


    def buildValueIndexDict(self, nums):
        value_indexes = {}
        for i in range(len(nums)):
            num = nums[i]
            if value_indexes.get(nums[i]) is None:
                value_indexes[nums[i]] = [i]
            else:
                value_indexes[nums[i]] += [i]
        
        return value_indexes