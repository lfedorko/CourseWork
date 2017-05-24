import numpy as np


def calculate_coefficient(newtable, k):
    t1 = np.sum(newtable, axis=1)
    t2 = 1 / t1
    C = np.sum(t2)
    c = list(map(lambda i: C / i, k))
    return t1, t2, C, c


def get_values(m, c):
    RealC = [0] * m
    f = c.copy()
    return RealC, f


def find_delta(c1, c2):
    e = []
    for i in range(len(c1)):
        e.append(c1[i] - c2[i])
    return e


def time_in_use(mashine):
    use = []
    for i in mashine:
        use.append(sum(i.values()))
    return use


def calculate_realC(c):
    Ci = []
    for i in c:
        temp = []
        temp.append(i // 1)
        temp.append(i % 1)
        Ci.append(temp)
    return Ci


def find_rand_delta(schedule, c, m):
    overfulfillment = []
    deficit = []

    for i in range(m):
        differenceFromReference = c - sum(schedule[i].values())

        if differenceFromReference < 0:
            deficit.append(abs(differenceFromReference))
            overfulfillment.append(0)
        else:
            overfulfillment.append(differenceFromReference)
            deficit.append(0)

    return overfulfillment, deficit


def calculate_sigma(c):
    e = [i % 1 for i in c]
    sigma = sum(e)
    return sigma, e
