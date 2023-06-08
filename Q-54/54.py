m = int(input())
n = int(input())
matrix_weight_value = [[0, 0]]
matrix_weight_value += [list(map(int, input().split())) for i in range(n)]
matrix = [[0 for j in range(m+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            continue
        elif matrix_weight_value[i][0] <= j:
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1]
                               [j-matrix_weight_value[i][0]] + matrix_weight_value[i][1])
        else:
            matrix[i][j] = matrix[i-1][j]
output_matrix = [[i, 0] for i in range(1, n+1)]
count = 0
while m != 0 or n != 0:
    if matrix[n][m] != matrix[n-1][m]:
        count += 1
        m -= matrix_weight_value[n][0]
        output_matrix[n-1][1] = 1
    n -= 1
print(count)
for line in output_matrix:
    for num in line:
        print(num, end=" ")
    print()