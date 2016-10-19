import os,sys,re
import subprocess

def NetCheck(ip):
    try:
        p = subprocess.Popen(["ping -c 1 -w 1 " + ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = p.stdout.read()
        regex = re.compile('100% packet loss')
        if len(regex.findall(out)) == 0:
            print ip + ': host up'
            return 'UP'
        else:
            print ip + ': host down'
            return 'DOWN'
    except:
        print 'NetCheck work error!'
        return 'ERR'
if __name__ == '__main__':
    NetCheck('192.168.1.88')
    NetCheck('192.168.6.9')
    NetCheck('192.168.1.90')

