#!/bin/bash -e

# sort the logs, pick those lines with timestamps, skip the timestamp, sort the frequency of the logs and output the top 3
sort /path/to/log | grep EST | uniq -c --skip-chars=100 | sort -rn | head -n 3 > tmp_file

# send the result to email as a notification
cat /path/to/log/tmp_file | mail -s "Top Errors Today" xxx1@example.com,xxx2@example.com -aFrom:xxx@example.com
