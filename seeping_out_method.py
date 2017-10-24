import numpy as np
import copy

matrix = np.array\
([
    [0, 1, 2, 3],
    [0, 2, 1, 6],
    [3, -1, 1, 3],
    [3, -1, 1, 3]
])

# [0, 1, 2, 3],
# [1, 2, 1, 6],
# [1, -1, 1, 3]

for i in range(matrix.shape[1]):

    if matrix[i][i] == 0:
        for j in range(matrix.shape[0]):
            temp = copy.deepcopy(matrix[j])
            matrix[j] = copy.deepcopy(matrix[0])
            matrix[0] = temp

    if matrix[i][i] == 0:
        break

    matrix[i] = matrix[i] / matrix[i][i]

    # for k in range(i + 1, matrix.shape[0]):
    #     matrix[k] = (matrix[i] * matrix[k][i] * -1) * matrix[k]


print(matrix)

#x = 3.0
#y = 1.0
#z = 1.0



