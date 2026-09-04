class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        previous_i = None
        nums.sort()


        for i, num in enumerate(nums):
            if num == previous_i:
                continue

            previous_i = num

            left = i + 1
            right = len(nums) - 1
            prev_left = None
            prev_right = None
            
            while left < right:
                result = num + nums[left] + nums[right] 

                if not result:
                    solutions.append([num, nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1]) and (right > left):
                        left += 1
                    
                elif result > 0: 
                    right -= 1
                    while (nums[right] == nums[right + 1]) and (right > left):
                        right -= 1

                else:
                    left += 1
                    while (nums[left] == nums[left - 1]) and (right > left):
                        left += 1

        return solutions
        