"""
Returns a string-array of s formatted in blocks with a specified length.
"""
def blockLines(s, blocks, blocklen):
    i = 0
    b = 0
    retval = ""
    for c in s:
        if i > 0:
            if i % blocklen == 0:
                retval += " "
                b += 1
            if b == blocks:
                retval = retval[:-1]
                retval += "\n"
                b = 0
        retval += str(c)
        i += 1
    return retval.splitlines()