

def invest(amount, interestes, months):
    #print (interestes)
    total_without_compose = 0

    for i in range(months):
        total_without_compose += amount * interestes
        print (total_without_compose)

def invest2(amount, interestes, months):
    #print (interestes)
    if(months == 0) : return amount
    total_without_compose = 0

    total_without_compose += amount * interestes
    return invest2(amount + (amount * interestes),interestes, months-1)





class Test():
    if __name__ == '__main__':
        #invest(1000000, 12, .10)
        interes = .11
        plazo = 12
        interest = interes/plazo
        result = invest2(1000000, interest, plazo)
        print(result)