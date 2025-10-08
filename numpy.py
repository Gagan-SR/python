# numpy_tutorial.py
# Run: python numpy_tutorial.py

import numpy as np

# 1. Create arrays
a = np.array([1, 2, 3, 4])
b = np.arange(5, 9)           # [5,6,7,8]
c = np.linspace(0, 1, 5)      # 5 values from 0 to 1

print("a:", a)
print("b:", b)
print("c:", c)

# 2. Reshape
m = np.arange(12).reshape(3, 4)
print("\nMatrix m (3x4):\n", m)

# 3. Element-wise ops and broadcasting
print("\na + 10:", a + 10)
print("a * 2:", a * 2)
print("a + b (element-wise):", a + b)

# 4. Linear algebra / dot product
v1 = np.array([1, 0, -1])
v2 = np.array([2, 3, 4])
print("\nDot product v1·v2:", np.dot(v1, v2))

# 5. Aggregations and statistics
print("\nmean of m along axis 0:", m.mean(axis=0))
print("sum of m:", m.sum())

# 6. Useful functions: mask, fancy indexing
mask = m % 2 == 0
print("\nEven entries in m:\n", m[mask])

# 7. Random numbers
rng = np.random.default_rng(seed=42)
samples = rng.normal(loc=0, scale=1, size=(3, 3))
print("\nRandom normal samples:\n", samples)
