"""
数据生成的主要逻辑
"""


import numpy as np


def generate_matrix(
    board_grid: int, unit_grid: int, unit_n: int, positions: list
) -> np.ndarray:
    """生成指定布局矩阵

    Args:
        board_grid (int): 布局板分辨率，代表矩形区域的边长像素数
        unit_grid (int): 矩形组件分辨率
        unit_n (int): 组件数
        positions (list): 每个元素代表每个组件的位置
    Returns:
        np.ndarray: 布局矩阵
    """
    m = np.zeros((board_grid, board_grid))
    for position in positions:
        unitPerRow = board_grid // unit_grid
        row_sta = ((position - 1) // unitPerRow) * unit_grid
        col_sta = ((position - 1) % unitPerRow) * unit_grid
        row_end = row_sta + unit_grid
        col_end = col_sta + unit_grid
        m[row_sta: row_end, col_sta: col_end] = 1
    return m
    raise NotImplementedError  # TODO: 实现布局矩阵的生成
