def insertion_sort_desc(arr):
    """
    Sorts the input array in-place in monotonically decreasing order 
    using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    # You can manually test with a sample list
    sample_list = [5, 2, 9, 1, 5, 6]
    print("Original list:", sample_list)
    
    sorted_list = insertion_sort_desc(sample_list)
    print("Sorted in decreasing order:", sorted_list)

    # Optional: Accept user input
    user_input = input("\nEnter numbers separated by spaces: ")
    user_list = list(map(int, user_input.strip().split()))
    user_sorted = insertion_sort_desc(user_list)
    print("Your sorted list (descending):", user_sorted)