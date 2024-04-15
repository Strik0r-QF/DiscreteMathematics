import numpy as np

def warshall(M: np.ndarray) -> np.ndarray:
    # 首先判断是否为方阵
    if M.shape[0] != M.shape[1]:
        raise ValueError("M is not square")

    # 初始化
    n = M.shape[0]
    closure = np.copy(M)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i, j] = closure[i, j] or (closure[i, k] and closure[k, j])

    return closure