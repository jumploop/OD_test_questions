def gcd(m, n):  #  求两个数的最大公约数,若为1则互为质数,返回TRUE
    if n == 0:
        m, n = n, m
    while m != 0:
        m, n = n % m, m
    if n == 1:
        return True
    return False


def gou_number(num=10):
    N = [i for i in range(1, num + 1)]
    M = [i * i for i in range(1, num + 1)]
    n = 0
    number = 0
    for i in M:
        for j in M[n:]:
            if i + j in M:
                a = N[M.index(i)]
                b = N[M.index(j)]
                c = N[M.index(i + j)]
                if gcd(a, b) and gcd(a, c) and gcd(b, c):  #  abc是否互为质数
                    number += 1
        n += 1
    return number


print(gou_number())