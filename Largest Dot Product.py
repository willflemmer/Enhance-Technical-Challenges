import numpy as np

def largest_dot_product(array1, array2):

    array1[::-1].sort()
    array2[::-1].sort()
    print(np.dot(array1, array2))

# Feel free to edit these arrays:
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 7])

largest_dot_product(arr_1, arr_2)