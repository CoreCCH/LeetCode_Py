class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nearest = 100000
        nums = sorted(nums)
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                pass
            else:
                l, r = i+1, len(nums) -1 
                while l < r and nearest != 0:
                    if nums[l]+nums[r]+a-target == 0:
                        return target
                    elif nums[l]+nums[r]+a>target:
                        if abs(nums[l]+nums[r]+a-target) < abs(nearest):
                            nearest = nums[l]+nums[r]+a-target
                        r-=1
                    elif nums[l]+nums[r]+a<target:
                        if abs(nums[l]+nums[r]+a-target) < abs(nearest):
                            nearest = nums[l]+nums[r]+a-target
                        l+=1
        return(target+nearest)