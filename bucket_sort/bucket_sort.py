from visualize import visualize_sorting


def bucket_sort(arr):
    visualize_sorting(arr)

    bucket = []

    num_buckets = 10

    for i in range(num_buckets):
        bucket.append([])

    for j in arr:
        index_b = min(int(num_buckets * j), num_buckets - 1)
        bucket[index_b].append(j)

    for i in range(num_buckets):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(num_buckets):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
            visualize_sorting(arr)
    return arr
