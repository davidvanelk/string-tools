import binascii
from convert import binary as binary
from fmt import blockformat, lineops

x = binary.stox("Hallo Welt! Dies ist ein Test und dies ist auch ganz gut so!")
x = blockformat.blockLines(x, 8, 4)
x = lineops.appendLines(x, "\t$\"", "\"")

for l in x:
    print(l)