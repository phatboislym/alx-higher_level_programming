#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    args = len(sys.argv)
    if args == 1:
        sum = 0
    else:
        for i in range(1, args):
            sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
