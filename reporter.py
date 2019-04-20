import datetime
import json
import subprocess
import sys
import time

try:
    import urllib2 as urllib
    
    version = 2
except ImportError:
    import urllib.request as urllib
    
    version = 3


def get_info():
    lines = subprocess.Popen("gpustat", shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL).stdout.readlines()
    lines = [line.decode('utf-8') for line in lines]
    return 0, lines


def send_info():
    err, data = get_info()
    data = json.dumps(data)
    if version == 3:
        data = bytes(data, 'utf8')
    try:
        headers = {'Content-Type': 'application/json'}
        request = urllib.Request(url=report_url, headers=headers, data=data)
        _ = urllib.urlopen(request)
        print("send info |", datetime.datetime.now())
    except urllib.URLError:
        print("fail to send |", datetime.datetime.now())


def keep_sending():
    print("Keep sending info to", base_url)
    while 1:
        send_info()
        time.sleep(time_interval)


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == 'test':
        print(get_info()[1])
    else:
        base_url = sys.argv[1]
        report_url = "http://" + base_url + "/post"
        try:
            time_interval = int(sys.argv[2])
        except (IndexError, ValueError):
            #  TODO: 做笔记：多异常的捕获，异常的层级关系
            time_interval = 180
        keep_sending()
