import binascii

# Converts a string given as parameter s to a byte-array.
def stobarr (s):
    b = bytearray()
    b.extend(map(ord, s))
    return b

# Converts a string given as parameter s to a hex-encoded string
def stox (s):
    return ''.join( [ "%02X" % ord( x ) for x in s ] ).strip()