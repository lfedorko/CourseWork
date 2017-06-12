from findValues import *
from outputData import *
from readData import *
from щдв.algorithms import *

if __name__ == '__main__':
    m, n, data = read_file('input.txt')

    print('Input data')
    k, p = convert_data(data)
    output_input_data(n, p, m, k)
    table = calculate_first_table(p, k)
    newtable = calculate_second_table(p, k, table)
    t1, t2, C, c = calculate_coefficient(newtable, k)
    output_ideal(c, k, C)


    RealC1, f = get_values(m, c)
    print()
    all1 = A1(m, n, table, RealC1,k)
    print()
    use1 = time_in_use(all1)
    overfulfillment, deficit = find_rand_delta(all1, C, m)
    output_result_values(use=use1, overfulfillment=overfulfillment, deficit=deficit)
    make_plot(all1)
    sigma, e = calculate_sigma(c)
    RealC2, f = get_values(m, c)
    all2 = A2(m, n, table, RealC2, f, p, k)
    use2 = time_in_use(all2)
    overfulfillment, deficit = find_rand_delta(all2, C, m)
    output_result_values(use=use2, overfulfillment=overfulfillment, deficit=deficit)
    make_plot(all2)
    x1, T = optimization1(sigma=sigma, e=e, k=k, C=C)
    result_of_opt1(T, k, x1, e)
    x2 = optimization2(k, e, sigma, C)
    result_of_opt2(T, k, x2, e)
