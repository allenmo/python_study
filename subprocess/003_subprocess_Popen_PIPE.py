import subprocess
import time

child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
time.sleep(2)
child.communicate("hello")

print "\n------------------------------\n"
child2 = subprocess.Popen(["ls"], stdin=subprocess.PIPE)
time.sleep(2)
child2.communicate(" -la")

