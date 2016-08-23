file = open('051_file_open_read.py', 'r')
lines = file.readlines()
for line in lines:
    #line = line.strip()
    print line
file.close()

