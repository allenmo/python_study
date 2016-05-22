import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file=""
output_file=""

def usage():
    text = "This is the help of 029_getopt.py\r\n"
    text += "usage1: python3 029_getopt.py -h\r\n"
    text += "usage2: python3 029_getopt.py -i inputfile.txt\r\n"
    text += "usage3: python3 029_getopt.py -o outputfile.txt\r\n"
    print(text)


for op, value in opts:
    if op == "-i":
        input_file = value
        print("input_file:%s"% input_file)
    elif op == "-o":
        output_file = value
        print("output_file:%s"% output_file)
    elif op == "-h":
        usage()
        sys.exit()


