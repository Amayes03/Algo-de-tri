from visualize import visualize_sorting


def selection_sort(arr):
    visualize_sorting(arr)
    
    n = len(arr)
    for i in range(n):
        # Initially, assume the first element of the unsorted part as the minimum.
        minimum = i

        for j in range(i+1, n):
            if (arr[j] < arr[minimum]):
                # Update position of the minimum element if a smaller element is found.
                minimum = j

        # Swap the minimum element with the first element of the unsorted part.     
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp
        visualize_sorting(arr)
    
    return arr
