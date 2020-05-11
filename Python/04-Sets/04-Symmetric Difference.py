if __name__ == '__main__':
    i = int(input())
    n = set(map(int, input().split()))
    j = int(input())
    m = set(map(int, input().split()))
    myset3 = m.symmetric_difference(n)
    print('\n'.join(map(str, sorted(myset3)))) 
    