from visualize import visualize_sorting


def pancake_sort(arr):
    visualize_sorting(arr)
    arr_len = len(arr)
    while arr_len > 1:
        mi = arr.index(max(arr[0:arr_len]))
        arr = arr[mi::-1] + arr[mi+1:len(arr)]
        arr = arr[arr_len-1::-1] + arr[arr_len:len(arr)]
        arr_len -= 1
        visualize_sorting(arr)
    return arr
