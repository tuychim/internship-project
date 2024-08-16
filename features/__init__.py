def string_counter(string: str):
    counter = 1
    result = ''

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            counter += 1
        else:
            result += f'{counter}{string[i - 1]}'
            counter = 1
    # Add the last group
    result += f'{counter}{string[-1]}'

    return result


str1 = 'aaabbbggggfffjjabc'
print(string_counter(str1))  # Output: 3a3b4g3f2j1a1b1c

# Example of sorted function usage
print(sorted([1, 6, 0]))  # Output: [0, 1, 6]
