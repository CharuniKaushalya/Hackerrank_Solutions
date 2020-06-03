import math
if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    ac = math.sqrt((ab*ab)+(bc*bc))
    mc = ac / 2.0
    angel_b_radian = math.acos(bc / (2*mc))
    angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
    output_str = str(angel_b_degree)+'°'
    print(output_str)