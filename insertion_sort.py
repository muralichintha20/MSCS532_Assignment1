def insertion_sort_desc(arr):
    # This function implements the Insertion Sort algorithm in descending order
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
if __name__ == "__main__":
    # Sample list to sort
    sample_list = [5, 2, 9, 1, 5, 6]

    print("Original list before sorting:", sample_list)  # Updated wording
    sorted_list = insertion_sort_desc(sample_list)
    print("Sorted in decreasing order:", sorted_list)