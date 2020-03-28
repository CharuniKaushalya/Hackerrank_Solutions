if __name__ == '__main__':
    sublist = []
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sublist.append([name,score])
        scorelist.append(score)
    mini = min([x for x in scorelist if x != min(scorelist)])
    sublist.sort()
    for m in sublist:
        if m[1] == mini:
            print(m[0])
