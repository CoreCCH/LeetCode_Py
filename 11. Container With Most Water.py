class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l_pos = 0
        r_pos = len(height)-1
        while(1):
            if r_pos>l_pos:
                if (height[l_pos]<height[r_pos]):
                    max_water = max(max_water, height[l_pos] * (r_pos-l_pos))
                    l_pos+=1
                elif (height[l_pos]>height[r_pos]):
                    max_water = max(max_water, height[r_pos] * (r_pos-l_pos))
                    r_pos-=1
                else:
                    max_water = max(max_water, height[r_pos] * (r_pos-l_pos))
                    l_pos+=1
                    r_pos-=1
            else:
                break
        return max_water




