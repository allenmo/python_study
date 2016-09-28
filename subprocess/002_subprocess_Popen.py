import subprocess
child1 = subprocess.Popen("ls -l|grep txt", stdout = subprocess.PIPE, shell = True)
child2 = subprocess.Popen(["wc"], stdin = child1.stdout, stdout=subprocess.PIPE)
out = child2.communicate()
print out
