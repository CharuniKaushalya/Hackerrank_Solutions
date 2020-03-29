if __name__ == '__main__':
    n = int(input())
    totlist = []
    for _ in range(n):
        name, *line = input().split()
        params = list(map(int, line))
        if name == "insert":
            totlist.insert(params[0], params[1])
        elif name == "print":
            print(totlist)
        elif name == "remove":
            totlist.remove(params[0])
        elif name == "append": 
            totlist.append(params[0])
        elif name == "sort": 
            totlist.sort()
        elif name == "pop": 
            totlist.pop()
        elif name == "reverse": 
            totlist.reverse()