def is_triangle(a, b, c):
    if (a + b > c ):
        if (a + c > b):
            if (b +c > a):
                return True
    return False
