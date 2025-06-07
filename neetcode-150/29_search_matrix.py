class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_number = -1
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row_number = mid
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][-1] < target:
                start = mid + 1

        if row_number == -1:
            return False

        start = 0
        end = len(matrix[0]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[row_number][mid] == target:
                return True
            elif matrix[row_number][mid] > target:
                end = mid - 1
            elif matrix[row_number][mid] < target:
                start = mid + 1

        return False

####################################################################################

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])
        while start <= end:
            print(start, end)
            mid = (start + end) // 2
            mid_element = matrix[mid // cols][mid % cols]
            if mid_element == target:
                return True
            elif mid_element > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
