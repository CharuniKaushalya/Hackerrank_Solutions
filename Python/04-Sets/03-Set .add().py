if __name__ == '__main__':
    s = set()
    for _ in range(int(input())):
        name = input()
        f = name.lower().strip()
        s.add(f)
    print(s)
    print(len(s))
    