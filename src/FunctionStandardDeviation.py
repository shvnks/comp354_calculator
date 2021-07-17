"""Calculating Standard Deviation."""


def power(x, y):
    """Power function."""
    return x**y


def standard_deviation(values):
    """Calculate standard deviation."""
    mean = 0
    for point in values:
        mean += point

    mean /= len(values)
    standard_deviation = 0

    for point in values:
        standard_deviation += power((point - mean), 2)

    return power((standard_deviation / len(values)), 0.5)


values = [1, 4, 0.5, 7, 3.4, 6.5, 3.4]
print(standard_deviation(values))  # gives 2.2843746074010665
