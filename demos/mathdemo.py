import numpy as np

# Create a numpy array.
nums = np.array([1, 2, 3, 4])
print(nums)

# Slicing returns a mutable view.
last_two_nums = nums[2:]
print(last_two_nums)

# array dimensions
nums_shape = nums.shape
len_shape = len(nums_shape)
print(f"Shape: {nums_shape}, Length: {len_shape}")

# unit matrix
# e = np.diag[1, 1, 1, 1]
m1 = 2 * np.identity(4)
m2 = np.diag([1, 2, 3, 4])
m3 = np.matmul(m1, m2)
print(m1)
print(m2)
print(m3)

