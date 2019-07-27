def find(l):
    result = []
    for a in l:
        if a % 2 == 0:
            result.append(a)
    return result

result = filter(lambda x : x % 2 == 0, l)
