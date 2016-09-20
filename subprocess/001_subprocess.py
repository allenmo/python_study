import subprocess

# pass args in a single string with no space, shell can be True or False
#subprocess.Popen('ls', shell=True)
#subprocess.Popen('ls', shell=False)

# pass args in string with space, need to set shell=True
#subprocess.Popen('ls -l', shell=True)
# if set sell=False, need to pass args in sequence
#subprocess.Popen(['ls','-l'], shell=False)
subprocess.Popen(('ls','-l'), shell=False)


