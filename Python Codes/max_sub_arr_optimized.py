def max_sub_array_of_size_k(k, arr):
    windowstart, windowSum = 0,0.0
    result = []
    max_sum = 0.0
    for windowend in range(len(arr)):

        windowSum +=arr[windowend]

        if windowend >= k-1:
            result.append(windowSum)
            max_sum = max(windowSum, max_sum)
            windowSum -=arr[windowstart]
            windowstart +=1
    return max_sum
if __name__ == '__main__':
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
