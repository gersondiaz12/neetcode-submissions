class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bigList = []
        # 1, 2, 4, 8, 10, 11, 12, 13, 14, 20, 30, 40 (target = 10)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                bigList.append(matrix[i][j])
        
        l, r = 0, len(bigList) - 1
        while l <= r:
            m = (l + r) // 2
            if bigList[m] > target:
                r = m - 1
            elif bigList[m] < target:
                l = m+ 1
            else:
                return True
        
        return False