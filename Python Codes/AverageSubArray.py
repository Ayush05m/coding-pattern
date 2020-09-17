from typing import List, Any, Union


def Average_sub_array(k, arr):
    result: List[Union[float, Any]] = []
    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i + k):
            _sum += arr[j]
        result.append(_sum / k)
    return result


if __name__ == '__main__':
    result = Average_sub_array(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))
