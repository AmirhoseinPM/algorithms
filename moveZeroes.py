from typing import List

class MoveZeroes:

    @staticmethod
    def bruteforceMove(self, A: List[int]) -> List[int]:
        output = []
        for i in A:
            # time complexity -> O(n)
            if i != 0:
                output.append(i)

        for i in range(len(A) - len(output)):
            # time complexity -> O(n-m)
            output.append(0)
        
        # total time comlexity -> O(n+n-m)= O(2n-m)
        # space comlexity -> output length -> O(n)
        return output
    
    @staticmethod
    def betterApproach(self, A: List[int]) -> List[int]:
        zero_index = 0  # space complexity -> O(1)
        for num in A:
            if num != 0:
                A[zero_index] = num
                zero_index += 1
        
        for i in range(zero_index,len(A)):
            A[i] = 0
        
        # time complexity -> O(n+m) : m = number of zero elements
        
        return A
            
    


print(MoveZeroes.bruteforceMove(A=[0,1,0,12,3]) == [1,12,3,0,0]) 
print(MoveZeroes.betterApproach(A=[0,1,0,12,3]) == [1,12,3,0,0]) 
