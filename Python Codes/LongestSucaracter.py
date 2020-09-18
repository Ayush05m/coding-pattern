def longest_substring_with_k_distinct(str1, k):
    windowstart = 0
    max_length = 0
    characterFrequency = {}
    # initiate a dictionary to track the frequency of character occurences
    for windowend in range(len(str1)):
        character = str1[windowend]
        if character not in characterFrequency:
            characterFrequency[character] = 0
        characterFrequency[character] += 1

        while len(characterFrequency) > k:
            toexcludecharcter = str1[windowstart]
            characterFrequency[toexcludecharcter] -= 1
            if characterFrequency[toexcludecharcter] == 0:
                del characterFrequency[toexcludecharcter]
            windowstart += 1
        max_length = max(max_length, windowend-windowstart + 1)
    return max_length
if __name__ == '__main__':
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
