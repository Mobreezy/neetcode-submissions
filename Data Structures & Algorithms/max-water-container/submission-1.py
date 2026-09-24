class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        bestArea = 0
        while l < r:
            width = r - l
            length = min(heights[r], heights[l])

            totalArea = length * width

            if bestArea < totalArea:
                bestArea = totalArea

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return bestArea