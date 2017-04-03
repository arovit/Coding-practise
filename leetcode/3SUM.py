#!/usr/bin/python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        hash_result = {}
        result_list = []
        if len(nums) < 3:
            return result_list
        for i in nums:
            count = hash_result.get(i, 0)
            count += 1
            hash_result[i] = count
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp_sum = nums[i] + nums[j]
                lookfor = -1 * temp_sum
                if (hash_result.get(nums[i], 0) > 0 and \
                        hash_result.get(nums[j], 0) > 0 and \
                            hash_result.get(lookfor, 0) > 0):
                    temp_array = [nums[i], nums[j], lookfor]
                    result_list.append(temp_array)
                    hash_result[nums[i]] -= 1
                    hash_result[nums[j]] -= 1
                    hash_result[lookfor] -= 1
        return result_list

solver = Solution()
input_list =  [-1, 0, 1, 2, -1, -4]
print solver.threeSum(input_list)
