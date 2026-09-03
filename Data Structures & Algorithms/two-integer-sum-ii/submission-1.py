class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = dict()
        
        for i, num in enumerate(numbers):
            compl = target - num

            if compl in map:
                return [map[compl] + 1, i + 1]

            map[num] = i

            

            