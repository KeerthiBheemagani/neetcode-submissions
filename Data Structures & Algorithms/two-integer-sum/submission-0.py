class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Mapper = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in Mapper:
                return [Mapper[diff], i]
            Mapper[n]=i
        
            
            


        
        

        