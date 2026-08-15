class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = []
        right_mul = []
        # add 1 as default
        left_mul.append(1)
        
        for i in range(1, len(nums)):
            temp = left_mul[i-1] * nums[i-1]
            left_mul.append(temp)
        
        # add 1 as default
        for i in range(len(nums)):
            right_mul.append(1)
                
        for i in range(len(nums) - 2, -1, -1):
            right_mul[i] = right_mul[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(left_mul[i] * right_mul[i])
        
        return res