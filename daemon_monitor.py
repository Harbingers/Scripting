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

def monitor_apache2():
    num = count_process("apache2")
    if(num > 0):
        print "apache2 is running !!!"
    else:
        print "apache2 is not running !!!"
        send_email("apache2", "web server 1", "is not running" )

monitor_apache2()
