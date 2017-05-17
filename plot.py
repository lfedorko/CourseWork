import numpy as np
import math as math

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
    C = np.sum(t2)
    c = list(map(lambda i: C / i, k))
    return t1, t2, c, C


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
    return(allmachine)

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
    return(allmachine)

def outputResult(all):
    for i in range(len(all)):
        print('Machine ', i + 1, all[i])

def findRandDelta(schedule, C, m):
    r = [0] * m
    delta = [0] * m
    for i in range(0, m):
        tmp = C - sum(schedule[i].values())
        if tmp < 0:
            delta[i] = math.fabs(tmp)
        else:
            r[i] = tmp
    print(r)
    print(delta)




if __name__ == '__main__':
    k = [1, 1.3, 1.5, 2, 2.3, 2.5]
    m = len(k)
    p = sorted([10, 9, 9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 4, 4, 3, 3, 2])
    p.reverse()
    n = len(p)
    print("n = {}\np = {}\nm = {}\nk = {}\n".format(n, p, m, k))
    table = calculateFirstTable(p, k)
    newtable = calculateSecondTable(p, k, table)
    t1, t2, c, C = calculateCoefficient(newtable)
    RealC, f = getValues(m, c)
    res1 = A1(m, n, table, RealC)
    #outputResult(res1)
    RealC, f = getValues(m, c)
    res2 = A2(m,n,table,RealC)
