from visualize import visualize_sorting


def insertion_sort(arr):
    visualize_sorting(arr)

    L = len(arr)
    if L <= 1:  # Si L = 0 ou 1, pas besoin de trier
        return

    for i in range(1, L):  # Commence à trier à partir de la deuxième valeur
        key = arr[i]  # La valeur à trier est dans key
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        visualize_sorting(arr)

    return arr
