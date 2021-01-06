class Solution:
    def findMin(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        
        if len(arr) == 1:
            return arr[0]
            
        if arr[left] < arr[right]: # there was no rotation
            return arr[0]
            
        while left < right:
            mid = left + (right-left)//2
            
            if arr[mid] > arr[right]:
                left = mid + 1
            elif arr[mid] < arr[right]:
                right = mid
        
        return arr[left]