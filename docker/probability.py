import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    tn = 1000
    p = 1000.0
    x = []
    y = []

    for n in range(1,tn):
        y_n = 1-pow((1-1/(n*p)),n)
        x.append(n)
        y.append(y_n)
        print "%d,%f" % (n,y_n)

    plt.title("n departs probability", fontproperties='SimHei')

    plt.ylim((0.03278, 0.033333))
    plt.xlim((0, 110))
    plt.xlabel(u'departs n', fontproperties='SimHei', fontsize=14)
    plt.ylabel(u'probability', fontproperties='SimHei', fontsize=14)

    plt.plot(x, y, color='red')
    plt.show()
