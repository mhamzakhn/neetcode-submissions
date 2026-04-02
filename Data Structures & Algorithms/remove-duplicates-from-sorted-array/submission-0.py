class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1, p2 = 0, 0

        while p2 < len(nums):

            if not p2 == len(nums) - 1 and nums[p2] == nums[p2 + 1]:
                p2 += 1
            elif p1 != p2:
                nums.pop(p1)
                p2 -= 1
            else:
                p1 += 1
                p2 += 1


        return len(nums)