import binascii
from convert import binary as binary
from fmt import blockformat, lineops
import sys

for param in sys.argv:
    print(param)

x = binary.stox("Hello World!")
x = blockformat.blockLines(x, 8, 4)
x = lineops.appendLines(x, "\t$\"", "\"")

for l in x:
    print(l)