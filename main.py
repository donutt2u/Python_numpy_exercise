import numpy as np

def create_zeros_array(size):
    return np.zeros(size)

def reverse_array(arr):
    return arr[::-1]

def set_fifth_element_to_one(arr):
    arr[4] = 1
    return arr

def change_last_row_to_ones(matrix):
    matrix[-1, :] = 1
    return matrix

def add_five_to_elements(matrix):
    matrix += 5
    return matrix

if __name__ == "__main__":
    # Example usage
    zeros_array = create_zeros_array(10)
    reversed_array = reverse_array(zeros_array.copy())
    fifth_element_set_to_one = set_fifth_element_to_one(reversed_array.copy())

    matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    last_row_changed_to_ones = change_last_row_to_ones(matrix.copy())
    elements_added_five = add_five_to_elements(matrix.copy())

    # Print or further manipulate the results as needed
    print("Zeros Array:", zeros_array)
    print("Reversed Array:", reversed_array)
    print("Fifth Element Set to One:", fifth_element_set_to_one)
    print("Matrix with Last Row Changed to Ones:", last_row_changed_to_ones)
    print("Matrix with Five Added to Elements:", elements_added_five)
