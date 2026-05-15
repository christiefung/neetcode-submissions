class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
                
                if current_streak > max_streak:
                    max_streak = current_streak
                
            elif num == 0:           
                current_streak = 0


        return(max_streak)