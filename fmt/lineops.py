"""
Format the lines (s) of a string, where it should begin with b and end with e
"""
def appendLines(s, b, e):
    retval = ""
    arr = s.splitlines()
    for l in arr:
        retval += b + l + e + "\n"
    return retval

def tabLines(s, tabs):
    retval = ""
    arr = s.splitlines()
    for l in arr:
        istr = ""
        for i in range(0, tabs):
            istr += "\t"
        retval += istr + l + "\n"
    return retval