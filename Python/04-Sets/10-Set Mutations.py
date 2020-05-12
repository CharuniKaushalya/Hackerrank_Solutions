if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        name, count = input().split()
        l = set(map(int, input().split()))
        if name == "intersection_update":
            s.intersection_update(l)
        elif name == "update":
            s.update(l)
        elif name == "symmetric_difference_update":
            s.symmetric_difference_update(l)
        elif name == "difference_update":
            s.difference_update(l)
    print(sum(s))