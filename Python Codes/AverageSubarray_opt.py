from typing import List, Any, Union


def Average_sub_array(k, arr) -> object:
    result: List[Union[float, Any]] = []
    # initialize window and starting point
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        # slide the window, we do not need to slide if we 've not hit the riquired #

        if windowEnd >= k - 1:
            result.append(windowSum / k)  # calculate the average
            windowSum -= arr[windowStart]
            windowStart += 1  # slide window
    return result


if __name__ == '__main__':
    result = Average_sub_array(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))
