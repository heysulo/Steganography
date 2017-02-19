import argparse
from time import gmtime, strftime


def stamp(mode=0):
    # 0 = info
    # 1 = warn
    # 2 = error
    msg = "INFO"
    if mode == 0:
        msg = "INFO"
    elif mode == 1:
        msg = "WARN"
    elif mode == 2:
        msg = "ERRO"
    return strftime("[" + msg + " %H:%M:%S" + "]", gmtime())


def main():
    print stamp(),"Initiating"
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output Filename", type=str)
    parser.add_argument("-i", "--input", help="Input Filename", type=str)
    args = parser.parse_args()

    if args.input:
        print stamp(), "Entering Steganography Encryption Mode"
    elif args.output:
        print stamp(), "Entering Steganography Decryption Mode"
    else:
        print stamp(2), "Parameters are not provided. Program is terminating"


main()
