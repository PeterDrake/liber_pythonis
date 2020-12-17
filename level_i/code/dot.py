import matplotlib.pyplot as plt


def dot_plot(xs):
    xs = sorted(xs)
    ys = []
    count = 0
    previous = None
    for x in xs:
        if x == previous:
            count = count + 1
        else:
            count = 0
        ys.append(count)
        previous = x
    plt.scatter(xs, ys)
    plt.xticks(list(set(xs)))
    plt.show()
    # plt.savefig('dot.png', bbox_inches='tight')


if __name__ == '__main__':
    import random
    xs = [x+y+z for x in range(1, 11) for y in range(1, 11) for z in range(1, 11)]
    dot_plot(xs)
    # dot_plot([random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) for _ in range(300)])
