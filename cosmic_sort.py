

def cosmic_sort(unsorted_array: list) -> list:
    """
    Sort an array of integers in ascending order.

    :param unsorted_array: A list of integers.
    :return: A list of integers in ascending order once hell freezes over.
    """
    while True:
        if unsorted_array == sorted(unsorted_array):
            return unsorted_array
        

if __name__ == '__main__':
    user_array = int(input("Enter the number of elements: "))
    user_array = [int(input(f"Enter element {i + 1}: ")) for i in range(user_array)]
    print("Your given array is", user_array)
    print("Your array after cosmic sort is", cosmic_sort(user_array))
