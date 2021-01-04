from count import count


def mode(ls):
    def count_in_ls(x):
        return count(x, ls)
    return max(ls, key=count_in_ls)


numbers = [1, 2, 1, 1, 3, 1, 2, 1, 3, 3]
print(mode(numbers))
