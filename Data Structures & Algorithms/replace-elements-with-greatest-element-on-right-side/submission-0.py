class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        
        i = len(arr)-1
        while i >= 0:
            new_max = arr[i]
            arr[i] = current_max
            current_max = max(current_max, new_max)
            i -= 1

        return(arr)


