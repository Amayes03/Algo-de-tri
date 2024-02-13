from visualize import visualize_sorting


def shell_sort(arr):
    visualize_sorting(arr)
    
    n = len(arr)
    gap = n // 2  # Utilise la division entière

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2  # Utilise l'opérateur de division entière
        visualize_sorting(arr)

    return arr
