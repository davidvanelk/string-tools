import binascii
from convert import binary as binary
from fmt import blockformat, lineops
import sys


x = str("")
filename = str("")
beginline = None
endline = None
blocks = 0
blocklength = 0
hexConversion = False
tabs = 0
outfile = str("")

for param in sys.argv[1:]:
    if not param.startswith('--'):
        if len(x) > 0:
            x += " "
        x += param
    else:
        param = param[2:]
        arr = param.split('=')
        if arr[0] == "file":
            filename = arr[1]
        elif arr[0] == "beginline":
            beginline = ''.join(arr[1:])
        elif arr[0] == "endline":
            endline = ''.join(arr[1:])
        elif arr[0] == "blocks":
            blockconfig = arr[1].split('x')
            blocks = int(blockconfig[0])
            blocklength = int(blockconfig[1])
        elif arr[0] == "hex":
            hexConversion = True
        elif arr[0] == "tabs":
            tabs = int(arr[1])
        elif arr[0] == "outfile":
            outfile = arr[1]
            
if len(filename) > 0:
    f = open(filename, "r")
    x = f.read()

if hexConversion:
    x = binary.stox(x)

if blocks > 0 and blocklength > 0:
    x = blockformat.blockLines(x, 8, 4)

if beginline != None:
    x = lineops.appendLines(x, beginline, "")
if endline != None:
    x = lineops.appendLines(x, "", endline)

if tabs > 0:
    x = lineops.tabLines(x, tabs)

if len(outfile) > 0:
    print("Writing to " + outfile + "...")
    f = open(outfile, "w")
    f.write(x)
else:
    print(x)