# attendancebot
This is a reworked attendancebot.py with new functionality:
-works with python3 and a csv file, without needing google sheets or google scripts anymore
-divides roster into seniors and non seniors to customize the number of remaining sessions needed to be attended in order to pass
-iterates a csv file and determines attendance rate, and how many of the remaining sessions still need to be attended in order to pass
-function to email each student with a detailed attendance update