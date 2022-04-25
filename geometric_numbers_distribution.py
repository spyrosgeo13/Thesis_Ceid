import numpy as np


def create_geometric_distribution_numbers_array():

    p= float(input("give the probability of success of individual trial: "))
    size = int(input("give the size of the array: "))

    g=np.random.geometric(p,size)