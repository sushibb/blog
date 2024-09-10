import bisect

def binary_search_lst(lst, key):
    a = 0
    b = len(lst)
    while a < b:
        c = (a + b) // 2
        if key(lst[c]):
            b = c
        else:
            a = c + 1
    return a

def binary_search(lower, upper, key):
    while lower < upper:
        mid = (lower + upper) // 2
        if key(mid):
            upper = mid
        else:
            lower = mid + 1
    return lower

def binary_search_float(lower, upper, diff, key):
    while upper - lower > diff:
        mid = (lower + upper) / 2
        if key(mid):
            upper = mid
        else:
            lower = mid
    return lower

if __name__ == '__main__':
    lst = [1, 3, 5, 13, 15, 16, 17, 19, 25, 30]
    print(binary_search_lst(lst, lambda x: x > 10))                    # 3
    print(binary_search_lst(lst, lambda x: x > 20))                    # 8
    print(binary_search_lst(lst, lambda x: x > 30))                    # 10 
    print(bisect.bisect_left(lst, 20))                                 # 8
    print(binary_search(0, 10**9, lambda x: x**2 > 300))               # 18
    print(binary_search_float(0, 10**9, 10**-6, lambda x: x**2 > 300)) # 17.320507694762455
