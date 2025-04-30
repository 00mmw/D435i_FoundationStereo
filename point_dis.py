import numpy as np

# 定义两个点的坐标
# A = [0.235591, 0.083028, 0.565245]
# B = [0.274143, 0.113256, 0.536437]

A = [0.049653,0.688464]
B = [0.216178,0.645401]

# 计算欧氏距离
distance = np.linalg.norm(np.array(A) - np.array(B))

# 输出结果
print(f"点 A 和点 B 之间的欧氏距离为: {distance:.6f}")