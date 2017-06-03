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
    print('\n----------------------------------------------------------------')
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
    print('\n----------------------------------------------------------------')
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


def optimization2(k, e, sigma, C):
    T = []
    for i in range(len(k)):
        T.append((C - k[i] * e[i]))
    print("T=", T)
    opt = [0] * len(k)
    x = [0] * len(k)
    while int(sigma) > 0:
        for i in range(len(k)):
            opt[i] = k[i]*(e[i] - x[i])
        index = opt.index(max(opt))
        x[index] += 1
        T[index] += k[index]
        sigma -= 1
    print("MyX = ", x)
    return x, T


def optimization1(sigma, e, k, C):
    T = []
    for i in range(len(k)):
        T.append((C - k[i] * e[i]))
    print("T=", T)
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
