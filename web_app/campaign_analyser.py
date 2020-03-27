def number_of_rev(series):
    m = 0
    for x in series:
        if x != 0 :
            m += 1
        else:
            break
    return m