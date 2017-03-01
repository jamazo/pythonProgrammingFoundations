import time
import webbrowser

print ("How many breaks do you want to take?")
total_breaks = int(raw_input("> "))

print ("Time Interval:")
hours = int(raw_input("hours: "))
break_count = 0

print ("This program started on "+time.ctime() )

while (break_count < total_breaks):
	time.sleep(hours*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=mJZ_DeOhetc")
	break_count += 1
