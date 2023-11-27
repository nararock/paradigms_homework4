from scipy.stats import pearsonr


def find_corr(x_in, y_in):
    avg_x = sum(x_in) / len(x_in)
    avg_y = sum(y_in) / len(y_in)

    def find_mult1(a, b):
        return (a - avg_x) * (b - avg_y)

    def find_mult2(a):
        return (a - avg_x) ** 2

    def find_mult3(b):
        return (b - avg_y) ** 2

    return sum(map(find_mult1, x_in, y_in)) / (sum(map(find_mult2, x_in)) *
                                               sum(map(find_mult3, y_in)))**0.5


x = [2, 1, 3, 9, 11, 12, 6, 15]
y = [1, 45, 7, 8, 23, 56, 1, 8]
answer = find_corr(x, y)
print(answer)
# проверка
print(pearsonr(x, y))


