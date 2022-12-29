import numpy as np
import matplotlib.pyplot as plt

words = ["books", "dad", "stock", "value", "singular", "estate", "decomposition"]
# 8个标题，7个关键字。记录每个关键字出现的次数，得到矩阵X。X中的每一行表示一个标题，每一列表示一个关键字
# 矩阵中的每个元素表示一个关键字在一个标题中出现的次数
X = np.array([[0, 2, 1, 0, 0, 0, 0],
              [2, 0, 0, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 1],
              [0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 1]])
U, s, Vh = np.linalg.svd(X)
# 输出奇异值矩阵U和shape
print("U=", U)
print("U.shape", U.shape)
# 输出奇异值矩阵及其shape
print("s=", s)
print("s.shape", s.shape)

# 输出右奇异矩阵Vh及其shape
print("Vh", Vh)
print("Vh.shape", Vh.shape)

# 通过奇异值选用关键词
plt.axis([-0.8, 0.2, -0.8, 0.8])

# 将原每个关键字有1*8的向量表示，现降维成为1*2的向量以便可视化
for i in range(len(words)):
    plt.text(U[i, 0], U[i, 1], words[i])

plt.show()