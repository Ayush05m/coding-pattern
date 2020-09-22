def length_of_longest_substring(str1, k):
    windowstart, max_length, max_count = 0,0,0
    frequency_tracker ={}
    for window_end in range(len(str1)):
        right = str1[window_end]
        if right not in frequency_tracker:
            frequency_tracker[right] = 0
        frequency_tracker[right] +=1
        max_count = max(max_count, frequency_tracker[right])

        if (window_end - windowstart + 1 - max_count > k ):
            left = str1[windowstart]
            frequency_tracker[left] -=1
            windowstart +=1

        max_length = max(max_length, window_end - windowstart + 1)
    return max_length

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()