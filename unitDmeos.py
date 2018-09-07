'''001-有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''


def demo1():
    num = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    print("%d %d %d" % (i, j, k))
                    num += 1
    print(num)


'''002-企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？'''


def demo2():
    i = float(input('净利润:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            i = arr[idx]
    print(r)


'''003-输入三个整数x,y,z，请把这三个数由小到大输出'''


def demo3():
    x = int(input("number 1 int:"))
    y = int(input("number 2 int:"))
    z = int(input("number 3 int:"))
    arr = [x, y, z]
    arr.sort()
    for v in arr:
        print(v)


'''004-斐波那契数列'''


def demo4(top):
    arr = [1,1]
    while arr[-1] < top:
        arr.append(arr[-1]+arr[-2])
    print(arr)


'''005-输出 9*9 乘法口诀表'''


def demo5():
    for i in range(1, 10):
        for j in range(1, i+1):
            print("%d * %d = %d\t" % (i, j, i*j), end="")
        print("")






