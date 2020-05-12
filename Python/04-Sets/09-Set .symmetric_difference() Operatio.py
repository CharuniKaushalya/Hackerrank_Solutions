if __name__ == '__main__':
    n = int(input())
    e = set(map(int, input().split()))
    m = int(input())
    f = set(map(int, input().split()))
    s = e.symmetric_difference(f)
    print(len(s))