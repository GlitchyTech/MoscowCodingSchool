def diamond(n):
    if type(n) != int or n < 0:
        return None
    if n%2 == 0:
        return None
    center = n*"*" + "\n"
    diamond_top = ""
    diamond_bottom = ""
    num_space = 1
    while n > 1:
        diamond_line = num_space * ' ' + (n-2) * '*'  + '\n'
        diamond_top += diamond_line
        diamond_bottom = diamond_line + diamond_bottom
        n = int(n-2)
        num_space += 1
    return diamond_bottom + center + diamond_top

print(diamond(7))

