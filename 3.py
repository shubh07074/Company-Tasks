import numpy as np
# Coefficient matrix A
A = np.array([[2, 1], 
              [3, 4]])
# Result vector b
b = np.array([5, 6])
# Solve for x (unknown variables)
x = np.linalg.solve(A, b)
# Output the solution
print("Solution:")
print(x)
