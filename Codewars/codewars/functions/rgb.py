def rgb(r, g, b):
    if r > 255:
        r = 255
    if r < 0:
        r = 0

    if g > 255:
        g = 255
    if g < 0:
        g = 0

    if b > 255:
        b = 255
    if b < 0:
        b = 0

    rstring = hex(r).split('x')[1].upper()
    if len(rstring)<2:
        result = "0" + rstring
    else:
        result = rstring
    gstring = hex(g).split('x')[1].upper()
    if len(gstring)<2:
        result += "0" + gstring
    else:
        result += gstring
    bstring = hex(b).split('x')[1].upper()
    if len(bstring)<2:
        result += "0" + bstring
    else:
        result += bstring
    return result

print rgb(255,255,255)
print hex(255)