#!/usr/bin/env python

import os
import subprocess

def count_process(process_name):
    ps = subprocess.Popen("ps -ef | grep -v grep | grep "+process_name+" | wc -l", shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    print(process_name, ' ', output)
    return output

def keepalive_process(process_name, limit):
    gap = limit - int(count_process(process_name))
    while gap > 0:
        os.system('php '+process_name)
        count_process(process_name)
        gap -= 1

keepalive_process(php_script_name1, 5)
