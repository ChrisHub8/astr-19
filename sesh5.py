import numpy as np
from tabulate import tabulate

def generate_table(start, end, num_points):
    x_values = np.linspace(start, end, num_points)
    y_values = np.sin(x_values)
    return list(zip(x_values, y_values))

def main():
    start = 0
    end = 2 * np.pi
    num_points = 1000
    table = generate_table(start, end, num_points)
    print(tabulate(table, headers=["x", "sin(x)"], floatfmt=".6f"))

if __name__ == "__main__":
    main()
