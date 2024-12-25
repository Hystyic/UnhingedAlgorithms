import itertools
import math
import time

global sorted_array


def compute_power_stack(lst):
    """
    Compute the power-stack for a list of integers. The computation is done right-to-left.
    """
    result = lst[-1]
    for num in reversed(lst[:-1]):
        result = num ** result
    return result


def sort_by_exponent_stack(nums):
    """
    Sort a list of integers >= 3 by finding the permutation that produces the highest power-stack.

    Args:
        nums (list): A list of integers >= 3.

    Returns:
        list: The permutation of the input list that produces the highest power-stack.
        float: The maximum power-stack value.
    """
    if not all(n >= 3 for n in nums):
        raise ValueError("All integers must be >= 3.")

    permutations = list(itertools.permutations(nums))

    max_value = -math.inf
    best_permutation = None

    for perm in permutations:
        power_stack_value = compute_power_stack(list(perm))
        if power_stack_value > max_value:
            max_value = power_stack_value
            best_permutation = perm

    return sorted(best_permutation), max_value


def compare_sort_times(nums):
    """
    Compare the time taken by sort_by_exponent_stack and Python's inbuilt sort function.

    Args:
        nums (list): A list of integers >= 3.

    Returns:
        dict: A dictionary containing the time taken by both methods.
    """
    start_time = time.time()
    result, value = sort_by_exponent_stack(nums)
    global sorted_array
    sorted_array = result
    power_sort_time = time.time() - start_time

    start_time = time.time()
    sorted(nums)
    inbuilt_sort_time = time.time() - start_time

    if power_sort_time == inbuilt_sort_time:
        print("HAIYAAHH!!! WHY SO WEAK SO WEAK GIVE BIGGER NUMBERS")
    return {
        "power_sort_time": power_sort_time,
        "inbuilt_sort_time": inbuilt_sort_time
    }


if __name__ == '__main__':
    nums = int(input("Enter the number of elements greater than or equal to 3: "))
    nums = [int(input(f"Enter element {i + 1}: ")) for i in range(nums)]
    times = compare_sort_times(nums)
    print(f"Sorted List: {sorted_array}")
    print(f"Power Sort Time: {times['power_sort_time']:.6f} seconds")
    print(f"Inbuilt Sort Time: {times['inbuilt_sort_time']:.6f} seconds")
