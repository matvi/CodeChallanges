



def fibonacy(n):
    f = []
    f.append(0)
    f.append(1)
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f

def fibonacy_space(n):
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


def fibonacy_reccursion(n):
    if(n == 2):
        return 1
    if (n == 1):
        return 0
    
    res = fibonacy_reccursion(n-1) + fibonacy_reccursion(n-2)
    return res

def fibonacy_memorize(n, f):
    if f[n] is not None:
        return f[n]
    if(n == 2 or n==1):
        return 1
    
    f[n] = fibonacy_memorize(n-1, f) + fibonacy_memorize(n-2, f)
    return f[n]


if __name__ == "__main__":
    # print(fibonacy(9))
    # print(fibonacy_space(9))
    # print(fibonacy_reccursion(9))
    print(fibonacy_memorize(8,[None]*9))