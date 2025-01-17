import numpy as np

# 座標
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])

# ユークリッド距離の計算
distance = np.sqrt(np.sum((a - b) ** 2))

print(f"ユークリッド距離: {distance}")
