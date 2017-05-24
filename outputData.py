import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def output_result_algorithm(result):
    for i in enumerate(result):
        print('Machine ', i[0] + 1, i[1])


def output_result_values(use, overfulfillment, deficit):
    print('Machine | |', ' S', '     | R', '         |Delta')
    for i in range(len(deficit)):
        print('   ', i + 1, '  | |', use[i], '   |', overfulfillment[i], '  ', deficit[i])


def output_ideal(normvalue, k, C):
    print('------------------')
    print('C: ', C, '|')
    print('------------------')
    print('---------------------------------------------------------------')
    print('i |', 'k(i)', '    | C(i)*', '               |[С(i)*]', '      |e(i)')
    print('---------------------------------------------------------------')
    for i in enumerate(normvalue):
        print(i[0] + 1, '|', k[i[0]], '     |', i[1], '        |', i[1] // 1, '       |', i[1] % 1)


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




    # print('key',npkey)

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
