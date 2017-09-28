"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)

>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""

def arb(*args):
    num_arg = len(args)
    return('The {} args are: {}'.format(num_arg, args))
print(arb)

def stats(*args):
    sum_arg = sum(args)
    return('Sum: {}'.format(sum_arg))
    max_arg = max(args)
    return('Max: {}'.format(max_arg))
    min_arg = min(args)
    return('Min: {}'.format(min_arg))
    avg_arg = int(sum_ars / len(args))
    return('Avg: {}'.format(avg_arg))
    range_arg = max_arg - min_arg
    return('Range: {}'.format(range_arg))
    return('Entries: {}'.format(len(args)))
print(stats)
