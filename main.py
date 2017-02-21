import argparse
from time import gmtime, strftime
import os.path
import PIL.Image
import sys

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
    parser.add_argument("-e", "--encrypt", help="Embed a message into an image", action='store_true')
    parser.add_argument("-d", "--decrypt", help="Extract a message from an image", action='store_true')
    parser.add_argument("-o", "--output", help="Output Filename", type=str)
    parser.add_argument("-i", "--input", help="Input Filename", type=str)
    args = parser.parse_args()

    if args.encrypt:
        print stamp(), "Entering Steganography Encryption Mode"
        if args.input:
            print stamp(),"Searching for the file",args.input
            if (os.path.isfile(args.input)):
                print stamp(),"The file",args.input,"Found"
                print stamp(),"Validating image"
                img = None
                try:
                    img =PIL.Image.open(args.input)
                except:
                    print stamp(2),"Image validation failed. The Image provided seems to be an invalid image"
                    print stamp(),"Exiting Program"
                    return
                print stamp(),"Valid",img.format,"image detected",img.size[0],"x",img.size[1]
                print stamp(),"Embeding Message",
                total_pixels = img.size[0]*img.size[1]*1.0
                for x in range(img.size[0]):
                    for y in range(img.size[1]):
                        print img.getpixel((x,y))

            else:
                print stamp(2),"The file", args.input, "was not found"
                print stamp(),"Exiting program"
                return
        else:
            print stamp(2),"No input file is provided"
            print stamp(),"Exiting Program"
            return
    elif args.decrypt:
        print stamp(), "Entering Steganography Decryption Mode"
    else:
        print stamp(2), "Required parameters are not provided. Program is terminating"


main()
