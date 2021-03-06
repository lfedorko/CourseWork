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


def A1(m, n, table, RealC, k):
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


def A2(m, n, table, RealC, f, p, k):
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
    print('\n----------------------------------------------------------------')
    print('Second optimization')
    T = []
    for i in range(len(k)):
        T.append((C - k[i] * e[i]))
    opt = [0] * len(k)
    x = [0] * len(k)
    counter =0
    sigma2 = round(sigma, 0)
    sigma2 = int(sigma2)
    print(int(sigma2))
    for i in range(sigma2):
        for i in range(len(k)):
            opt[i] = k[i]*(e[i] - x[i])
        index = opt.index(max(opt))
        x[index] += 1
        T[index] += k[index]
        counter +=1
    print(counter)
    print("X = ", x)
    return x


def optimization1(sigma, e, k, C):
    print('\n----------------------------------------------------------------')
    print('First optimization')
    T = []
    for i in range(len(k)):
        T.append((C - k[i] * e[i]))
    FirstT = T.copy()
    Tq = T.copy()
    for i in range(len(k)):
        Tq[i] += k[i]
    x = [0] * len(k)
    sigma2 = round(sigma, 0)
    print(int(sigma2))
    sigma2 = int(sigma2)
    print(int(sigma2))
    for i in range(sigma2):
        index = Tq.index(min(Tq))
        Tq[index] += k[index]
        x[index] += 1
    for i in range(len(k)):
        T[i] += x[i] * k[i]
    print("X = ", x)
    return x, FirstT





