class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max = 
        #  height = [1,8,6,2,5,4,8,3,7]
        #            | |

        l = 0
        end_of_container = 0
        r = len(heights)-1

        while l < r:
            # choose between the smaller heights * the right to get the longest width
            # get the biggest container out of them
            # if we find a height greater than or equal to the left 
            # increment left by1
            # else
            # decrement right by 1
            area = min(heights[l],heights[r]) * (r-l)
            end_of_container = max(end_of_container, area)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return end_of_container