test_list = ['hello, world', 'hello, earth']


def string_comparing(first_string, second_string):
    first_string = first_string.split(',')
    second_string = second_string.split(',')
    answer = [word_1 for word_1 in first_string for word_2 in second_string if word_1 == word_2]
    return answer


print(string_comparing(test_list[0], test_list[1]))
