def mode(data):
    def count_in_ls(x):
        return data.count(x)
    return max(data, key=count_in_ls)


numbers = [1, 2, 1, 1, 3, 1, 2, 1, 3, 3]
print(mode(numbers))
