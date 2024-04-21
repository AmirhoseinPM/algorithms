from typing import List

class VlaidMountainArray:
    @staticmethod
    def validate(self, A: List[int]) -> bool :
        """
            check that elements start ascending and end descending
            example : [1, 2, 3, 4, 3, 2, 1] -> True
        """
        if (len(A) < 3):
            return False

        i = 1

        # check ascending elements from start to valid indexs
        while ((i<len(A)) and (A[i]> A[i-1])):
            i += 1

        if ((i==1) or (i==len(A))):
            # when i do not changed or last index 
            return False
        
        while ((i<len(A)) and (A[i]<A[i-1])):
            i += 1
        
        return (i==(len(A)))
        


print(VlaidMountainArray.validate(A=[1, 2, 1]))
print(VlaidMountainArray.validate(A=[1, 2, 3, 4, 3, 2, 1, 2, 3]))
