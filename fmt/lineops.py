"""
Format the lines (s) of an array, where it should begin with b and end with e
"""
def appendLines(s, b, e):
    i = 0
    for l in s:
        s[i] = b + l + e
        i += 1
    return s