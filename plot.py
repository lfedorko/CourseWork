from algorithms import *
from findValues import *
from outputData import *
from readData import *

if __name__ == '__main__':
    m, n, data = read_file('input.txt')

    k, p = convert_data(data)
    output_input_data(n, p, m, k)
    table = calculate_first_table(p, k)
    newtable = calculate_second_table(p, k, table)
    t1, t2, C, c = calculate_coefficient(newtable, k)
    RealC1, f = get_values(m, c)
    all1 = A1(m, n, table, RealC1)
    use1 = time_in_use(all1)
    tmp = calculate_realC(RealC1)
    RealC, f = get_values(m, c)
    all2 = A2(m, n, table, RealC, f, p)
    overfulfillment, deficit = find_R_and_delta(all2, C, m)
    print()
    output_result_values(c, overfulfillment, deficit)
    sigma, e = find_e_sigma(c)
    OptimizationAl1(sigma, e, k, C)


