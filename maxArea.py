from typing import List

class maxAreaCalculator:
    """
        algorithms with array example
    """
    @staticmethod
    def bruteforce(self, heights: List[int]) -> int:
        """
            calculate all available area and find max
            Time complexity O(n^2)
            Space complexity O(1)
        """
        max_area = 0
        for i in range(0,len(heights)):
            for j in range(1,len(heights)):
                height = min(heights[i], heights[j])
                width = abs(j - i)
                if max_area < (height * width):
                    max_area = (height * width)
        return max_area

    @staticmethod
    def betterWay (height: List[int]) -> int:
        """
            change array index base on height of index
            Time complexity O(n^2)
            Space complexity O(1)
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while (left<right):
            max_area = max(max_area, ( min(height[left], height[right]) * abs(left - right)))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
