# -*- coding=utf8 -*-
__author__ = 'CubeLin'


def sort(num_list):
    """ Input type: list
        Return type: list
    """

    list_len = len(num_list)

    for i in xrange(list_len):
        for j in xrange(list_len - i - 1):
            if num_list[j] > num_list[j + 1]:
                # swap numbers here
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list


def search(sorted_list, target):
    """ Input: sorted_list: sorted list in ascending order(list)
               target:      target to search for(integer)
        Return: index of target(integer)
    """

    list_len = len(sorted_list)
    low_index = 0
    high_index = list_len - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) / 2
        mid_num = sorted_list[mid_index]

        if mid_num < target:
            low_index = mid_index + 1
        elif mid_num > target:
            high_index = mid_index - 1
        else:
            return mid_index
    return -1


# Entry
if __name__ == '__main__':
    # sort
    input_string = raw_input('Please input numbers separated by spaces: ')
    input_list = [int(item) for item in input_string.split()]
    sorted_list = sort(input_list)
    print 'Result: %s' % ' '.join(map(str, sorted_list))

    # search
    input_target = raw_input('Please input the target to search for: ')
    result = search(sorted_list, int(input_target))
    if result == -1:
        print 'Not found.'
    else:
        print 'The index of %s is %d.' % (input_target, result)
