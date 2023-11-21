



#recursive
def factorial(n):
    if n == 1 :
        return 1
    return n * factorial(n-1)

#loop
def factorial2(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res



if __name__ == "__main__":
    print(factorial2(5))
    print(factorial(5))