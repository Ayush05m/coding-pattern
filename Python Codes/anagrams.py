def find_string_anagrams(str1, pattern):

    window_start = 0
    matched = 0
    frequency_tracker = {}
    # create a map of actual pattern in place :

    for chr in pattern:
        if chr not in frequency_tracker:
            frequency_tracker[chr] = 0
        frequency_tracker[chr] += 1
    result_indexes = []
    for windowend in range(len(str1)):
        right = str1[windowend]
        if right in frequency_tracker:
            frequency_tracker[right] -= 1
            if frequency_tracker[right] == 0:
                matched += 1

        if matched == len(frequency_tracker):
            result_indexes.append(window_start)

        if windowend >= len(pattern) - 1:
            left = str1[window_start]
            window_start += 1
            if left in frequency_tracker:
                if frequency_tracker[left] == 0:
                    matched -= 1
                frequency_tracker[left] += 1

    return result_indexes


def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()