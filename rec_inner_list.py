import sys


res = []

sys.setrecursionlimit(10000)


def inner_list(lst, i, savelst):
    if isinstance(lst, list):
        for elem in lst:
            if isinstance(elem, list):
                break
        else:
            if lst not in res:
                res.append(lst)
            else:
                raise Exception
    for i in range(i, len(lst)):
        if isinstance(lst[i], list):
            inner_list(lst[i], i + 1, savelst)
        else:
            inner_list(savelst, i + 1, savelst)
    try:
        inner_list(lst[i - 1], i, savelst)
    except:
        try:
            if i >= len(lst) + 2:
                i = 0
                for i in range(i, len(lst)):
                    if isinstance(lst[i], list):
                        inner_list(lst[i], i, savelst)

        except:
            pass


savelst = [[[[[[[[[[[11], [12]], [13]], [14]], [15]], [16]], [17]]]]],
           [3, 4, [5, 6, 7, [9, 10]], [1001, [1023, [[242], 1024, [1025, 10126], [1053]]]]], [77, [177]], [99],
           [33, [22]]]
try:
    inner_list(savelst, 0, savelst)
except:
    pass
print(res)
