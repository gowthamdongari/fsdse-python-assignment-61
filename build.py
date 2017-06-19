def solution(list_of_nums):
    """Enter Code Here"""
    even = 0
    odd = 0
    d = {}
    for i in list_of_nums:
        if(i % 2 == 0):
            even = even + 1
        else:
            odd = odd + 1

    d['ODD'] = odd
    d['EVEN'] = even
    return d

solution([1, 2, 3, 5, 8, 9])
