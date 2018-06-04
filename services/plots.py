import matplotlib.pyplot as plt


def plot_pivots(X, pivots, date_arr):
    plt.xlim(min(date_arr), max(date_arr))
    plt.ylim(X.min() * 0.99, X.max() * 1.01)
    plt.plot(date_arr, X, 'k:', alpha=0.5)
    plt.plot(date_arr[pivots != 0], X[pivots != 0], 'k-')
    plt.scatter(date_arr[pivots == 1], X[pivots == 1], color='g')
    plt.scatter(date_arr[pivots == -1], X[pivots == -1], color='r')
    plt.show()
