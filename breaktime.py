# Break Time
# Opens input website every input time

# By PK
# Udacity Programming Foundations
# August 2016

import time
import webbrowser


break_amount = 3
time_between = 5
break_count = 0
break_site = "https://www.youtube.com/"

print "This program started at: " + time.strftime("%I:%M:%S %PM")
while break_count < break_amount:
	time.sleep(time_between)
	print "Break " + str((break_count + 1)) + "  at: " + time.strftime("%I:%M:%S %PM")
	webbrowser.open(break_site)
	break_count += 1