import numpy as np
from scipy.sparse import random
from scipy.sparse.linalg import eigs
# Step 1: Create a large sparse matrix
n = 1000  # Matrix size (1000x1000)
density = 0.01  # 1% non-zero entries
A = random(n, n, density=density, format='csr', dtype=np.float64)  # Sparse matrix
# Step 2: Compute the 5 largest eigenvalues and their eigenvectors
k = 5  # Number of eigenvalues/vectors to compute
eigenvalues, eigenvectors = eigs(A, k=k)
# Output the results
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
