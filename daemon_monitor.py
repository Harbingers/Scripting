#!/usr/bin/env python

import subprocess
import smtplib
import os
import time

def count_process(process_name):
    ps = subprocess.Popen("ps -ef | grep -v grep | grep "+process_name+" | wc -l", shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    print(process_name, ' ', output)
    return output
    
def get_cpu():
    output = os.getloadavg()
    print output[2]
    return output[2]

def send_email(process_name, server_name, type):
    SERVER = "localhost"
    FROM = "monitors@" + server_name
    TO = ["receiver@example.com"] # need to be a list
    SUBJECT = "Here is an Update from " + server_name
    TEXT = process_name +" "+ type
    SUBJECT = server_name + " " + process_name + " " + type
    message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)

def monitor_cpuload():
    num = get_cpu()
    if(num > 5):
        print "cpu load is larger than 5 !!!"
        send_email("cpu load", "web server 1", "is larger than 5")
    else:
        print "cpu load is smaller than 5 !!!"

def monitor_apache2():
    num = count_process("apache2")
    if(num > 0):
        print "apache2 is running !!!"
    else:
        print "apache2 is not running !!!"
        send_email("apache2", "web server 1", "is not running" )

def monitor_ntp():
    num = count_process("ntp")
    if(num > 0):
        print "ntp is running !!!"
    else:
        print "ntp is not running !!!"
        send_email("ntp", "web server 1", "is not running")

monitor_cpuload()
monitor_apache2()
monitor_ntp()
