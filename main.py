import numpy as np
from src import Polynomial
from src.read_csv import read_csv

if __name__ == '__main__':
    read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_53000.csv')

    coeffs = np.array([1,0,0])
    polynom = Polynomial(coeffs)
    print(polynom.evaluate(3))
    print(polynom.roots())




