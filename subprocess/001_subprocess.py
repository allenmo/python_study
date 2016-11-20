import subprocess
import time

# pass args in a single string with no space, shell can be True or False
#subprocess.Popen('ls', shell=True)
#subprocess.Popen('ls', shell=False)

# pass args in string with space, need to set shell=True
#subprocess.Popen('ls -l', shell=True)
# if set sell=False, need to pass args in sequence
#subprocess.Popen(['ls','-l'], shell=False)

subprocess.Popen(('ls','-la'), shell=False)

print "-------------------------------"
child = subprocess.Popen(["ping", "www.baidu.com", "-c", "3"])
# child.wait()
print "child OBJ:", child
print "child.pid:", child.pid
time.sleep(0.5)
print "child.poll:", child.poll
# child.kill()
# child.send_signal(child.SIGTERM)
child.terminate()

child.wait()
