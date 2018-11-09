import binascii

# Converts a string given as parameter s to a byte-array.
def stobarr (s):
    b = bytearray()
    b.extend(map(ord, s))
    return b

# Converts a string given as parameter s to a hex-encoded string
def stox (s):
    x = binascii.hexlify(stobarr(s))
    return x