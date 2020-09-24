def find_permutation(str1, pattern):
    windowstart = 0
    matched = 0
    frequency_tracker = {}

    for element in pattern:
        if element not in frequency_tracker:
            frequency_tracker[element] = 0
        frequency_tracker[element] += 1

    for windend in range(len(str1)):
        right = str1[windend]
        if right in frequency_tracker:
            frequency_tracker[right] -= 1
            if frequency_tracker[right] == 0:
                matched += 1

        if matched == len(frequency_tracker):
            return True

        if windend >= len(pattern) - 1:
            left = str1[windowstart]
            windowstart += 1
            if left in frequency_tracker:
                if frequency_tracker[left] == 0:
                    matched -= 1
                frequency_tracker[left] += 1

    return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()


