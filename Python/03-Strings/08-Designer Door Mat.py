if __name__ == '__main__':
    n, m = map(int, input().split())
    l = n // 2

    #top part
    for i in range(0,l):
        print(('.|.'*(2*i+1)).center(m,'-'))


    #middle part
    print('WELCOME'.center(m,'-'))

    #bottom part
    for i in range(l,0,-1):
        print(('.|.'*(2*i-1)).center(m,'-'))