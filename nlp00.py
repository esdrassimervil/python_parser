import re
import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Missing filename: specify a file to read.", file=sys.stderr)
        sys.exit(0)
    pat = re.compile("[.?!][ \n\t]")
    dict = {}
    all = ""
    try:
        with open(sys.argv[1], 'r') as fd:
            for line in fd:
                s = line.replace("\n"," ")
                all += s
    except:
        print(f'Cannot open {sys.argv[1]}.', file=sys.stderr)
        sys.exit(0)
        
    n = 0
    for x in pat.split(all):
        print("{0:3d}: {1:s}".format(n,x))
        n += 1
