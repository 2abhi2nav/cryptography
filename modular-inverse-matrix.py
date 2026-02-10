
import numpy as np
modval = 26

m = np.array([[3, 5, 7, 2], [1, 4, 7, 2], [6, 3, 9, 17], [13, 5, 4, 16]])

m_inv = np.zeros((4, 4))
if np.linalg.det(m) != 0:
    m_inv = np.linalg.inv(m)

m_modinv = np.zeros((4, 4))
for i in range(len(m_inv)):
    for j in range(len(m_inv[i])):
        m_modinv[i][j] = m_inv[i][j] % modval

print(m_modinv)
