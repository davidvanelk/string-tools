"""
Format the lines (s) of a string, where it should begin with b and end with e
"""
def appendLines(s, b, e):
    retval = ""
    if isinstance(s, str):
        s = s.splitlines()
    for l in s:
        retval += b + l + e + "\n"
    return retval

"""
Prepend tabs to each line.
"""
def tabLines(s, tabs):
    retval = ""
    if isinstance(s, str):
        s = s.splitlines()
    for l in s:
        istr = ""
        for i in range(0, tabs):
            istr += "\t"
        retval += istr + l + "\n"
    return retval