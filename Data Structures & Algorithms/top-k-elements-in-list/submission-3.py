class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = dict()
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
            
        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        solution = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                solution.append(num)

                if len(solution) == k:
                    return solution
