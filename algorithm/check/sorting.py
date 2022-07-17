import time


# Sequence sort checker
def is_sorted(data: list):
    """
    Checks whether sequence has ascending sorting
    :param data: list sequence
    :return:
    """
    sort_status = False
    if len(data) <= 1:
        sort_status = True
        return data
    elif len(data) > 1 and sort_status is False:
        scope = len(data) - 1
        for n in range(scope - 1):
            if data[scope] > data[scope - 1]:
                scope -= 1
                sort_status = True
            else:
                sort_status = False
                break
        if scope == 1 and sort_status is True:
            print('Data is sorted')
            return data
        else:
            print('Data is not sorted')
            return data


def is_palindrome_inverted(load):
    data = load.lower().replace(' ', '').replace(',', '').replace("'", '')
    step_left = 0
    step_right = 0
    mid = len(data) // 2

    while step_right < mid:
        if (len(data) % 2) == 0 and step_left == 0:
            step_left += 1
        leftside = data[mid - step_left]
        rightside = data[mid + step_right]
        if leftside == rightside:
            step_left += 1
            step_right += 1
        else:
            return print(f'{load} is not a palindrome')
    return print(f'{load} is palindrome')


def is_palindrome(load):
    data = load.lower().replace(' ', '').replace(',', '').replace("'", '')
    for character in range(len(data) // 2):
        if data[character] != data[- character - 1]:
            print('Is not palindrome')
            break
        else:
            continue
    return print(f'{load} is palindrome')


# TESTING ZONE
test_1 = 'Do gees see God'
test_2 = 'А роза упала на лапу Азора1'
test_3 = 'Каак'
test_4 = "Madam, I'm Adam"

start = time.time()
# is_palindrome_inverted(test_4)
is_palindrome(test_4)
print(f'Calc time: {round(((time.time() - start) * 1000), 3)} milliseconds \n')