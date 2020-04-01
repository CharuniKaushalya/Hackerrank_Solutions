def print_rangoli(n):
    l = n 
    alphbet = list(map(chr, range(97, 97+l)))
    alphbet.reverse()

    sublist = []

    #top part
    for i in range(0,l):
        s = alphbet[i]
        for j in range(i-1,-1,-1):
            s = alphbet[j]+"-"+s+'-'+alphbet[j]
        # print(s)
        sublist.append(s)
    
    lenl = len(sublist[l-1])
    for i in range(0,l):
        print((sublist[i]).center(lenl,'-'))

    sublist.reverse()
    for i in range(1,l):
        print((sublist[i]).center(lenl,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)