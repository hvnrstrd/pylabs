def unique(lst):
    uniquelst = []
    for x in lst:
        if x not in uniquelst:
            uniquelst.append(x)
    return uniquelst

print(unique([3,4,2,2,4,2,1,4]))