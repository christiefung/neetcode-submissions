class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 #left pointer
        n = len(nums) #right pointer
        while i < n:
            if nums[i] == val:
                n = n-1
                nums[i] = nums[n]
        
            else: 
                i +=1
              
        return(n)    

        