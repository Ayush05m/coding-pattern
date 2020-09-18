def longest_unique_subString(str1):
    windowstart = 0
    max_length = 0
    index_map = {}
    for windowend in range(len(str1)):
        right = str1[windowend]
        if right in index_map:
            windowstart = max(windowstart, index_map[right] + 1)
        index_map[right] = windowend
        max_length = max(max_length, windowend - windowstart + 1)
    return max_length


if __name__ == '__main__':
    print("Length of the longest substring: " + str(longest_unique_subString("aabccbb")))
    print("Length of the longest substring: " + str(longest_unique_subString("abbbb")))
    print("Length of the longest substring: " + str(longest_unique_subString("abccde")))
