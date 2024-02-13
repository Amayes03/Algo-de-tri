from visualize import visualize_sorting


def quick_sort(arr):
    visualize_sorting(arr)
    
    elements = len(arr)
    
    # Base case
    if elements < 2:
        return arr  # Retourne le tableau non modifié pour le cas de base
    else:
        current_position = 0  # Position of the partitioning element
        for i in range(1, elements):  # Partitioning loop
            if arr[i] <= arr[0]:
                current_position += 1
                temp = arr[i]
                arr[i] = arr[current_position]
                arr[current_position] = temp

        temp = arr[0]
        arr[0] = arr[current_position]
        arr[current_position] = temp  # Brings pivot to its appropriate position
    
        left = quick_sort(arr[0:current_position])  # Sorts the elements to the left of pivot
        right = quick_sort(arr[current_position + 1:elements])  # Sorts the elements to the right of pivot

        arr = left + [arr[current_position]] + right  # Merging everything together
        visualize_sorting(arr)
    
    return arr
