def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Create a table to store the minimum scalar multiplications
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the table with maximum values
    for i in range(n):
        dp[i][i] = 0
    
    # Fill the table using dynamic programming
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = float('inf')  # Initialize with infinity
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # Reconstruct the optimal parenthesization
    def optimal_parenthesization(i, j):
        if i == j:
            return f'M{str(i)}'
        else:
            k = dp[i][j]
            for x in range(i, j):
                if dp[i][x] + dp[x + 1][j] + matrices[i - 1][0] * matrices[x][1] * matrices[j][1] == k:
                    return f'({optimal_parenthesization(i, x)} x {optimal_parenthesization(x + 1, j)})'
    
    # Return the optimal parenthesization and minimum scalar multiplications
    return optimal_parenthesization(1, n - 1), dp[1][n - 1]

# Get the number of matrices from the user
n = int(input("Enter the number of matrices: "))

# Get the dimensions of each matrix from the user
matrices = []
for i in range(n):
    dimensions = input(f"Enter the dimensions of matrix {i + 1} (rows columns): ").split()
    dimensions = (int(dimensions[0]), int(dimensions[1]))
    matrices.append(dimensions)

parenthesization, min_scalar_mult = matrix_chain_multiplication(matrices)

print("Optimal Parenthesization:", parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_mult)

'''
Explanation of the dynamic programming approach:

* We create a table dp to store the minimum scalar multiplications required for different subproblems.
* We fill the table using a bottom-up approach. For each chain length from 2 to n-1,
* we calculate the minimum scalar multiplications for each subproblem.
* We reconstruct the optimal parenthesization using the table by tracking the split point k that minimizes the cost.

Time Complexity Analysis:

The time complexity of the dynamic programming algorithm is O(n^3), where n is the number of matrices.
The space complexity is O(n^2) to store the dp table.

Efficiency for Large Instances:

This algorithm is efficient for small to moderately sized instances of the problem
but may become slow for very large instances due to its cubic time complexity.
For larger instances, more efficient algorithms such as Strassen's algorithm for matrix multiplication
or parallelization techniques might be preferred.
''' 


