from typing import List

class MinBoatsNumber:
    @staticmethod
    def minCalculate(self, peoples: List[int], limit: int) -> int:
        
        peoples.sort()  # this create Time Complexity = O(N log(N)) ,and Space Complexity = O(N)
        boats = 0
        smallest = 0
        biggest = len(peoples) - 1

        while (smallest <= biggest):

            if smallest == biggest:
                boats += 1
                break
            
            if peoples[smallest] + peoples[biggest] <= limit:
                smallest += 1

            biggest -= 1
            boats += 1

        return boats

