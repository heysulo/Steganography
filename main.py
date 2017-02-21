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


def texttobin(txt):
    res = ""
    for letter in list(txt):
        tmp = str(bin(ord(letter))[2:])
        tmp = "0"*(8-len(tmp))+tmp
        res+= tmp
    return res+"0"*(3-len(res)%3)


def bintotext(bintxt):
    res = ""
    for i in range(len(bintxt)/8):
        res += str(chr(int(bintxt[i*8:i*8+8],2)))
    return res


def readbin(x):
    return int(bin(x)[-1])


def encodepixel(pixel,txt):
    #print stamp(),pixel,"->",txt
    return (int(str(bin(pixel[0]))[2:-1]+txt[0],2),int(str(bin(pixel[1]))[2:-1]+txt[1],2),int(str(bin(pixel[2]))[2:-1]+txt[2],2))


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
                space = img.size[1]*img.size[0]*3/8
                print stamp(),"Valid",img.format,"image detected",img.size[0],"x",img.size[1]
                print stamp(),"Space available for you data : ",space, "Bytes/Characters"
                print stamp(),"Enter Secret Message : ",
                txt =texttobin(raw_input())
                print stamp(),"Embeding Message"
                out = img
                total_pixels = img.size[0]*img.size[1]*1.0
                marker = 0
                for x in range(img.size[0]):
                    for y in range(img.size[1]):
                        selection = "000"
                        if marker<len(txt):
                            selection=txt[marker:marker+3]
                        marker+=3
                        out.putpixel((x,y),encodepixel(img.getpixel((x,y)),selection))
                out.save("out.jpg")
                print stamp(),"Message Embedding Success!"
                print stamp(),"Exiting Program"
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
                space = img.size[1]*img.size[0]*3/8
                print stamp(),"Valid",img.format,"image detected",img.size[0],"x",img.size[1]
                print stamp(),"Reading Embeded Message"
                out = img
                total_pixels = img.size[0]*img.size[1]*1.0
                marker = 0
                for x in range(img.size[0]):
                    for y in range(img.size[1]):
                        selection = "000"
                        if marker<len(txt):
                            selection=txt[marker:marker+3]
                        marker+=3
                        out.putpixel((x,y),encodepixel(img.getpixel((x,y)),selection))
                out.save("out.jpg")
                print stamp(),"Message Embedding Success!"
                print stamp(),"Exiting Program"
            else:
                print stamp(2),"The file", args.input, "was not found"
                print stamp(),"Exiting program"
                return
        else:
            print stamp(2),"No input file is provided"
            print stamp(),"Exiting Program"
            return
    else:
        print stamp(2), "Required parameters are not provided. Program is terminating"


main()
