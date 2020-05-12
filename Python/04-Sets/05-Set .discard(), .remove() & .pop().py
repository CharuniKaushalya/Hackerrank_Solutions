if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        name = input()
        if "remove" in name:
            command, params = name.split()
            s.remove(int(params))
        elif "discard" in name:
            command, params = name.split()
            s.discard(int(params))
        elif name == "pop": 
            s.pop()
    print(s)
    print(sum(s))