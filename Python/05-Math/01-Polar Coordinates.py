# import cmath
# import math

# if __name__ == '__main__':
#     s = input().split("+")
#     x = int(s[0])
#     y = int(s[1][0])
#     #print(cmath.phase(complex(x, y)))
#     print(math.atan(y/x))
#     print(abs(complex(x,y)))
import cmath
z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])
    
