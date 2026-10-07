class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val=-1
        n=len(arr)
        ans =[0]*n
        for i in range(n)[::-1]:
            ans[i]=max_val
            max_val= max(arr[i],max_val)
        return ans
            


        