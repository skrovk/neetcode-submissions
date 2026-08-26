class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, num in enumerate(nums):
            key = target - num
            key_i = map.get(key) 

            if key_i is not None:
                return [key_i, i]

            map[num] = i