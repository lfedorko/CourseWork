import numpy as np


# %matplotlib inline


# первая таблица
def calculateFirstTable(p, k):
    table = []
    for j in range(len(k)):
        row = []
        for i in range(len(p)):
            row.append(p[i] * k[j])
        table.append(row)
    table = np.array(table)
    table = table.T
    return table


def calculateSecondTable(p, k, table):
    newtable = []
    for i in range(table.shape[0]):
        row = []
        for j in range(table.shape[1]):
            row.append(1 / table[i, j])
        newtable.append(row)
    newtable = np.array(newtable)
    return newtable


def calculateCoefficient(newtable):
    t1 = np.sum(newtable, axis=1)
    t2 = 1 / t1
    C = int(round(np.sum(t2)))
    c = list(map(lambda i: C / i, k))
    return t1, t2, c


def getValues(m, c):
    RealC = [0] * m
    f = c.copy()
    return RealC, f


def A2(m, n, table, RealC):
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

    outputResult(allmachine)

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

    outputResult(allmachine)

def outputResult(all):
    for i in range(len(all)):
        print('Machine ', i + 1, all[i])


if __name__ == '__main__':
    k = [1, 2,3,4,5]
    m = len(k)
    p = sorted([20,15,12,10,9,7,4,5,4,3,2,2,1,1])#, 9, 12, 15, 18, 21, 27, 40])
    p.reverse()
    n = len(p)
    print("n = {}\np = {}\nm = {}\nk = {}\n".format(n, p, m, k))
    table = calculateFirstTable(p, k)
    newtable = calculateSecondTable(p, k, table)
    t1, t2, c = calculateCoefficient(newtable)
    RealC, f = getValues(m, c)
    A1(m, n, table, RealC)
    RealC, f = getValues(m, c)
    print()

    A2(m,n,table,RealC)

