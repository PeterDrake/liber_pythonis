def mode(ls):
    def count_in_ls(x):
        return ls.count(x)
    return max(ls, key=count_in_ls)


numbers = [1, 2, 1, 1, 3, 1, 2, 1, 3, 3]
print(mode(numbers))
