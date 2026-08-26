class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, num in enumerate(nums):
            map[num] = i

        for i, num in enumerate(nums):
            key = target - num
            
            key_i = map.get(key) 

            if not key_i:
                continue

            if i == key_i:
                continue

            return [i, key_i]

            
            
