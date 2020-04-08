def solve(s, k):
    res = [s[i: i+k] for i in range(0,len(s),k) ] 
    for i in range(len(res)):
        result = "".join(dict.fromkeys(res[i]))
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    solve(string,k)