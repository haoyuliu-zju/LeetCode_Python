class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]

        """
        for i in range(k):
        	reset = 0
        	temp = nums[0]
        	for j in range(len(nums)):
        		if temp < nums[j]:
        			temp = nums[j]
        			reset = j
        	nums[reset] = float('-Inf') 
        return temp
        """
		