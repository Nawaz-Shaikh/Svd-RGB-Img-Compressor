import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import my_svd

A = imread('high.jpg').astype(float)

# Split into R, G, B channels
R = A[:, :, 0]
G = A[:, :, 1]
B = A[:, :, 2]

# Apply SVD to each channel
Ur, Sr, Vr = my_svd.SVD(R, full_matrices=True)
Ug, Sg, Vg = my_svd.SVD(G, full_matrices=True)
Ub, Sb, Vb = my_svd.SVD(B, full_matrices=True)

# Choose how many singular values to keep
k = 100

# print("R shape:", R.shape)
# print("Ur:", Ur.shape)
# print("Sr:", Sr.shape)
# print("Vr:", Vr.shape)


# Reconstruct each channel
R_recon = Ur[:, :k] @ np.diag(Sr[:k]) @ Vr[:k, :]
G_recon = Ug[:, :k] @ np.diag(Sg[:k]) @ Vg[:k, :]
B_recon = Ub[:, :k] @ np.diag(Sb[:k]) @ Vb[:k, :]

# Stack channels back
A_recon = np.stack((R_recon, G_recon, B_recon), axis=2)

# Clip values to [0, 255] for display
A_recon = np.clip(A_recon, 0, 255).astype(np.uint8)

# Show reconstructed image
plt.imshow(A_recon)
plt.axis('off')
plt.title(f'SVD Reconstruction with k={k}')
plt.show()


#svd.SVD(R,full_matrix=True)
