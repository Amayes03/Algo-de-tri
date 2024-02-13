from visualize import visualize_sorting


def odd_even_sort(arr):
    visualize_sorting(arr)
    
    # Unsorted array
    n = len(arr)
    Sorted = 0
    while Sorted == 0:
        Sorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                Sorted = 0
                  
        for i in range(0, n-2, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                Sorted = 0
                visualize_sorting(arr)
    
    return arr
