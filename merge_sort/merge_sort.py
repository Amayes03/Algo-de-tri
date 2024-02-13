from visualize import visualize_sorting


def merge_sort(arr):
    visualize_sorting(arr)
    
    if len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]  # Diviser le tableau en deux moitiés
        Right = arr[mid:]

        merge_sort(Left)  # Trier la première moitié
        merge_sort(Right)  # Trier la deuxième moitié

        i = j = k = 0  # Indices pour parcourir les deux moitiés et le tableau principal

        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        # Pour toutes les autres valeurs restantes dans Left et Right
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1
            visualize_sorting(arr)

    return arr
