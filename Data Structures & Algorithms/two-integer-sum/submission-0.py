class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i, value in enumerate(nums):
            v=target-value
            if v in result:
                return [result[v], i]
            result[value]=i
           
        