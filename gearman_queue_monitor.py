#!/usr/bin/python

import sqlite3

# get result from sqlite (gearman queue)
conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()
cur.execute('''select function_name, count(*) from table_name group by function_name;''')
rows = cur.fetchall()

# send out an email
import smtplib
SERVER = "localhost" # use local postfix

FROM = "gearman@example.com"
TO = ["receiver@example.com"] # need to be a list

SUBJECT = "Here is an Update from the Gearman Queue"

TEXT = "Here is an Update from the Gearman Queue \n "
for row in rows:
  TEXT += row[0]
  TEXT += "     "
  TEXT += str(row[1])
  TEXT += "\n"

print TEXT
# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

import os

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()

conn.close()
