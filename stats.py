from __future__ import division
from collections import Counter

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''.splitlines()

columns = [column.strip() for column in data[0].split(',')]

fns = [str, float, float]

x = [{key: fn(value) for key, fn, value in zip(columns, fns, line.split(','))} for line in data[1:]]

alcohol = [d["Alcohol"] for d in x]
tobacco = [d["Tobacco"] for d in x]


def range(series):
    return min(series), max(series)


def mean(series):
    return sum(series) / len(series)


def mode(series):
    d = Counter(series)
    return d.most_common(1)[0][0]


def median(series):
    n = len(series)
    start, end = int(n  / 2), int((n + 1) / 2)
    return sum(series[start:end + 1]) / 2


def variance(series):
    m = mean(series)
    hat_iter = ((s - m) for s in series)
    return sum(s * s for s in hat_iter)


def stdev(series):
    return (variance(series) ** 0.5) / (len(series) - 1)


def main():
    for name, series in (("alcohol", alcohol), ("tobacco", tobacco)):
        print("The range for {0} is {1} to {2}".format(name, *range(series)))
        print("The mean of {0} is {1}".format(name, mean(series)))
        print("The mode of {0} is {1}".format(name, mode(series)))
        print("The median of {0} is {1}".format(name, median(series)))
        print("The variance of {0} is {1}".format(name, variance(series)))
        print("The standard deviation of {0} is {1}".format(name, stdev(series)))

if __name__ == '__main__':
    main()
