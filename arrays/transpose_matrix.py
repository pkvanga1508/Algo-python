def transposeMatrix(matrix):
    # Write your code here.
    result = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            result[col][row] = matrix[row][col]

    return result

################################################

def transposeMatrix_2(matrix):

    result = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)
    return result
