# -*- coding: utf-8 -*-
# @File    : 最速下降法.py
# @Time    : 2021/4/14
# @Author  : laipinyan
from sympy import *


def main():
    global init
    print('初始点：', init)
    for i in range(nub_iter):
        print('---第{}次迭代---'.format(i+1))
        g1 = diff(f, x).subs(x, init[0])  # 对x偏导
        g2 = diff(f, y).subs(y, init[1])  # 对y偏导
        new_x = init[0] + t*(-g1)
        new_y = init[1] + t*(-g2)
        f_new = f.subs([(x, new_x), (y, new_y)])  # 新函数
        grad_new = diff(f_new, t)  # 对t偏导
        t_val = nsolve(grad_new, 0)  # 求t
        init = (new_x.subs(t, t_val), new_y.subs(t, t_val))  # 新点
        f_value = f.subs([(x, init[0]), (y, init[1])])  # 目标函数值
        print('x = ', init)
        print('目标函数值：', f_value)


if __name__ == '__main__':
    x, y, t = symbols('x1'), symbols('x2'), symbols('t')
    f = x ** 2 + 3 * y ** 2  # 设置初始函数
    init = (2, 1)  # 设置初始点
    nub_iter = 5  # 设置迭代次数
    main()
