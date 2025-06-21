import numpy as np

def SVD(A, full_matrices=True):
    m, n = A.shape

    u = A @ A.T
    eigvals_U, eigvecs_U = np.linalg.eigh(u)

    idx = np.argsort(eigvals_U)[::-1]
    eigvals_U = eigvals_U[idx]
    eigvecs_U = eigvecs_U[:, idx]

    diagnol_vals = np.sqrt(np.maximum(eigvals_U, 0))

    U = eigvecs_U


    nonzero_idx = diagnol_vals > 1e-10 
    sigma = np.diag(1 / diagnol_vals[nonzero_idx])
    V_partial = sigma @ U[:, nonzero_idx].T @ A
    V = np.zeros((n, n))
    V[:V_partial.shape[0], :] = V_partial

    if full_matrices:
        U = np.pad(U, ((0, 0), (0, n - m)), mode='constant') if m < n else U
        V = V  
    else:
        k = min(m, n)
        U = U[:, :k]
        diagnol_vals = diagnol_vals[:k]
        V = V[:k, :]

    return U, diagnol_vals, V
