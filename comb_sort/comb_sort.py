from visualize import visualize_sorting


def comb_sort(arr):

    visualize_sorting(arr)
    gap = len(arr)
    swap = True

    while gap > 1 or swap:
        swap = False
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        for i in range(0, len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swap = True
                visualize_sorting(arr)
    return arr
