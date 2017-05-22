def read_file(filename):
    with open(filename, 'r') as f:
        m, n = [int(x) for x in next(f).split()]
        data = [[float(x) for x in line.split()] for line in f]
    return m, n, data


def convert_data(data):
    k = data[0]
    p = data[1]
    p = sorted(p)
    p.reverse()
    return k, p

