def mean_square(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Списки должны быть одинаковой длины"

    mean_sq = 0

    for i in range(len(arr1)):
        diff = abs(arr1[i] - arr2[i])
        mean_sq += diff ** 2

    mean_sq /= len(arr1)

    return mean_sq
