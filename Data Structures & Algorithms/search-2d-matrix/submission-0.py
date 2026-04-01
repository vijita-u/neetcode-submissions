class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = 0
        ml, mr = 0, len(matrix)-1
        while ml <= mr:
            mm = (ml + mr) // 2
            if target >= matrix[mm][0] and target <= matrix[mm][-1]:
                row = mm
                break
            elif target > matrix[mm][-1]:
                ml = mm+1
            elif target < matrix[mm][0]:
                mr = mm-1
            else:
                return False
        
        l = 0
        r = len(matrix[row])-1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False
            


    