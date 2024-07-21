def longest(s):
    cur = 1
    indcur = 0
    indmax = 0
    max_count = 0
    for i in range(len(s) - 1):
        if s[i] <= s[i+1]:
            cur += 1
        else:
            if max_count < cur:
                max_count = cur
                indmax = indcur
            cur = 1
            indcur = i + 1

    if max_count < cur:
        max_count = cur
        indmax = indcur
    #print(s[indmax:indmax + max_count])
    return s[indmax:indmax + max_count]
