# Given a (N + 1) * N Matrix, assign each column of 1st row of matrix, the subsequent row of Matrix.

# Input : test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
# Output : {5: [2, 0, 9], 8: [5, 4, 2], 10: [2, 3, 9]}
# Explanation : 5 paired with 2nd row, 8 with 3rd and 10 with 4th


test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

for i in range(len(test_list) - 1):
    res = {test_list[0][i] :  test_list[i + 1]}
    print(res)


