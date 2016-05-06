# check if there is any update in the git master branch. 
# if yes, do some actions (deploying to staging environment etc)

#!/usr/bin/env python
import os
import commands

output = commands.getstatusoutput('cd repo_name; git pull origin master')
if "Already up-to-date" in output[1]:
    print "Already up-to-date, do nothing"
else:
    print "There is update in this branch, do some action now"
    os.system('./action.sh')
