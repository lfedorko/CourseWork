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


def optimization2(k, c, sigma):
    output = [0] * len(k)
    T = [0] * len(k)
    for i in range(len(k)):
        T[i] = (c[i] - c[i] // 1) * k[i]
    while int(sigma) > 0:
        T_test = T.copy()
        for i in range(len(k)):
            T_test[i] -= k[i]

        index = T_test.index(max(T_test))

        T[index] -= k[index]
        output[index] += 1
        # print(sigma)
        sigma -= 1
    return output, T


def optimization1(sigma, e, k, C):
    T = []
    for i in range(len(k)):
        T.append(round((C - k[i] * e[i]), 2))
    Tq = T.copy()
    for i in range(len(k)):
        Tq[i] += k[i]
    x = [0] * len(k)
    for i in range(int(sigma)):
        index = Tq.index(min(Tq))
        Tq[index] += k[index]
        x[index] += 1
    for i in range(len(k)):
        T[i] += x[i] * k[i]
    p = [i - C for i in T]

    return x, p
