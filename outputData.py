import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from terminaltables import AsciiTable


def output_result_algorithm(result):
    for i in enumerate(result):
        print('Machine ', i[0] + 1, i[1])


def output_result_values(use, overfulfillment, deficit):
    machine = []
    for i in range (len(deficit)):
        machine.append(i + 1)
    resultTable = list(zip( ['Machine'] + machine, ['Sum'] + use, ['R(i)'] + overfulfillment, ['Delta Δ(i)'] +deficit))
    table = AsciiTable(resultTable)
    print(table.table)




def output_ideal(normvalue, k, C):
    print('------------------')
    print('C: ', C, '|')
    print('------------------')
    machine = []
    for i in range(len(k)):
        machine.append(i+1)
    int_c = []
    e = []
    #fraction_e = []
    for i in normvalue:
        int_c.append(i //1)
        e.append(i % 1)
        l =i % 1
    resultTable = list(zip(['i'] + machine, ['Ki'] + k, ['Ci*'] + normvalue, ['[Ci*]'] + int_c, ['e']+ e))
    table = AsciiTable(resultTable)
    print(table.table)
    print('------------------')
    print(' Delta (Σe): ', sum(e), '|')
    print('------------------')

def result_of_opt1(T, k, x, e):

    xe = [0] * len(k)
    kxe = [0] * len(k)
    Tq = [0] * len(k)
    for i in range(len(k)):
        xe[i] = x[i] - e[i]
        kxe[i] = k[i] * xe[i]
        Tq[i] = T[i] + x[i]*k[i]
    print('max| (k(x-e)) | = {} ' .format(max(list(map(abs, kxe)))))
    resultTable = list(zip(['T'] + T, ['Ki'] + k, ['x'] + x,  ['e'] + e, ['x - e'] +xe , ['k(x-e)'] + kxe, ['T*'] + Tq))
    table = AsciiTable(resultTable)
    print(table.table)

def result_of_opt2(T, k, x, e):

    xe = [0] * len(k)
    kxe = [0] * len(k)
    Tq = [0] * len(k)
    for i in range(len(k)):
        xe[i] = e[i] - x[i]
        kxe[i] = k[i] * xe[i]
        Tq[i] = T[i] + k[i]*x[i]
    print('max| (k(e - x)) | = {} ' .format(max(list(map(abs, kxe)))))
    resultTable = list(zip(['T'] + T, ['Ki'] + k, ['x'] + x,  ['e'] + e, ['e - x'] +xe , ['k(e-x)'] + kxe, ['T*'] + Tq))
    table = AsciiTable(resultTable)
    print(table.table)



def output_input_data(n, p, m, k):
    print("n = {0}\np = {1}\nm = {2}\nk = {3}\n".format(n, p, m, k))


def make_plot(data):
    value = []
    for i in data:
        value.append(list(i.values()))

    key = []
    for i in data:
        key.append(list(i.keys()))

    data = pd.DataFrame(value)  # , index=title)
    key = pd.DataFrame(key)

    data = data.fillna(0)
    key = key.fillna(0)

    npdf = data.T.as_matrix()
    npkey = key.T.as_matrix()

    ind = np.arange(data.shape[0])

    title = []
    for j in range(data.shape[0] + 1):
        numer = ('Machine {}'.format(j))
        title.append(numer)

    # print('npdf',npdf)






    width = 1
    bottom_size = [0] * data.shape[0]
    fig, ax = plt.subplots()

    for i in range(data.shape[1]):
        for j in range(data.shape[0]):
            p1 = plt.bar(ind[j], npdf[i, j], width, bottom=bottom_size[j], edgecolor='black')  # ,label=npkey[i,j])
            # red_patch = mpatches.Patch(label=str(npkey[i, j]))
            # plt.legend(handles=[red_patch])
        bottom_size += npdf[i]
    # ax.set_xticklabels(title)



    # plt.legend(p1, npkey)
    # red_patch = mpatches.Patch(label=npkey)
    # plt.legend(handles=[red_patch])
    plt.show()
