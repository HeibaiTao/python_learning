"""练习1: 矩阵计算器

实现一个简单的矩阵计算器，支持:
    - 矩阵加法
    - 矩阵乘法
    - 矩阵转置
    - 行列式计算
    - 逆矩阵
"""

import numpy as np                                # 导入 numpy 模块


def matrix_add(a, b):                             # 定义矩阵加法函数
    """两个矩阵相加"""                            # 函数说明
    return a + b                                  # 逐元素相加


def matrix_multiply(a, b):                        # 定义矩阵乘法函数
    """矩阵乘法（点积）"""                        # 函数说明
    return a @ b                                  # 使用 @ 运算符


def matrix_transpose(a):                          # 定义转置函数
    """返回矩阵的转置"""                          # 函数说明
    return a.T                                    # 使用 .T 属性


def matrix_determinant(a):                        # 定义行列式函数
    """计算方阵的行列式"""                        # 函数说明
    return np.linalg.det(a)                       # 使用 linalg.det


def matrix_inverse(a):                            # 定义逆矩阵函数
    """计算方阵的逆矩阵"""                        # 函数说明
    return np.linalg.inv(a)                       # 使用 linalg.inv


# 测试
if __name__ == "__main__":                        # 判断是否直接运行
    A = np.array([[1, 2], [3, 4]])                # 创建测试矩阵 A
    B = np.array([[5, 6], [7, 8]])                # 创建测试矩阵 B

    print("A =\n", A)                             # 打印矩阵 A
    print("B =\n", B)                             # 打印矩阵 B
    print("A + B =\n", matrix_add(A, B))          # 测试加法
    print("A @ B =\n", matrix_multiply(A, B))     # 测试乘法
    print("A^T =\n", matrix_transpose(A))         # 测试转置
    print(f"det(A) = {matrix_determinant(A):.1f}")  # 测试行列式
    print("A⁻¹ =\n", matrix_inverse(A))           # 测试逆矩阵
