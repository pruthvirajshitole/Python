def sort(l):
    sorted_l = []
    while l:
        maximum = l[0]
        for i in l:
            if i<maximum:
                maximum=i
        sorted_l.append(maximum)
        l.remove(maximum)

    return sorted_l
