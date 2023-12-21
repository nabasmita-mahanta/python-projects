# Write a python program to add two matrices.

A = [[10, 5, 7],
     [9, 7, 6],
     [16, 5, 7]]
B = [[3, 4, 8],
     [6, 2, 9],
     [5, 7, 1]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(r)
