import numpy as np
from findValues import *
from outputData import *


def calculate_first_table(p, k):
    table = []
    for j in range(len(k)):
        row = []
        for i in range(len(p)):
            row.append(p[i] * k[j])
        table.append(row)
    table = np.array(table)
    table = table.T
    return table


def calculate_second_table(p, k, table):
    newtable = []
    for i in range(table.shape[0]):
        row = []
        for j in range(table.shape[1]):
            row.append(1 / table[i, j])
        newtable.append(row)
    newtable = np.array(newtable)
    return newtable


def A1(m, n, table, RealC):
    print('Algorithm 1')
    allmachine = []
    for i in range(0, m):
        machine = {}
        allmachine.append(machine)

    for j in range(n):
        index = RealC.index(min(RealC))
        RealC[index] += table[j][index]
        allmachine[index].update({j + 1: table[j][index]})

    output_result_algorithm(allmachine)
    return allmachine


def A2(m, n, table, RealC, f, p):
    print('Algorithm 2')
    allmachine = []
    for i in range(0, m):
        machine = {}
        allmachine.append(machine)

    for j in range(0, n):
        index = f.index(max(f))  # index with max f
        RealC[index] += table[j][index]  # fill C
        f[index] -= p[j]
        allmachine[index].update({j + 1: table[j][index]})

    output_result_algorithm(allmachine)
    return allmachine
