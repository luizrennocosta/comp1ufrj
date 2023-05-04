def f(a,b):
    if a < 2:
        print('?')
        condition_1=True
    else:
        k = 2
        condition_1=True
        while k < a:
            if a%k == 0:
                condition_1=False
            k +=1
                
    if b < 2:
        print('?')
        condition_2=True
    else:
        k = 2
        condition_2=True
        while k < b:
            if b%k == 0:
                condition_2=False
            k += 1
    
    if b >= a:
        if b < a:
            print('??')
    else:
        a,b = b,a
        
    k=1
    while k <= b:
        if b%k == 0 and a%k == 0:
            m = k
            print('???')
        k += 1
    return condition_1, condition_2, m

if __name__ == '__main__':
    print(f(8, 12))