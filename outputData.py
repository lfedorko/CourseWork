def output_result_algorithm(result):
    for i in enumerate(result):
        print('Machine ', i[0] + 1, i[1])


def output_result_values(normvalue, overfulfillment, deficit):
    print('Machine |', '|  R', '| Delta', '| Whole part', '| Real part', '| Imagine part ')
    for i in enumerate(normvalue):
        print('   ', i[0] + 1,
              '  | |',   round(overfulfillment[i[0]], 2),
              '  ', round(deficit[i[0]], 2)
              , '       ', round(i[1], 2),
              '     ', round(i[1] // 1, 2),
              '       ', round(i[1] % 1, 2))


def output_input_data(n, p, m, k):
    print("n = {0}\np = {1}\nm = {2}\nk = {3}\n".format(n, p, m, k))
