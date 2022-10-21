import sys, csv

#create email_report str
email_report = ""

#search string for "22" to sort out the seniors
# (the year they will graduate is built into their email addresses)
word_search = str(22)
seniors = []
everyone_else = []

#read csv, and split on "," the line
file = open("attendance.csv", newline='')
csvreader = csv.reader(file, delimiter=',')
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
line_count = (len(rows))

#sort entries into two new lists: seniors and non-seniors
#first, initialize the lists
file = open("attendance.csv")
csvreader = csv.reader(file)
header = next(csvreader)
while line_count >= 1:
    for row in rows:
        if word_search in row[1]:
            seniors.append(row)
            line_count -= line_count 
        else:
            everyone_else.append(row)
            line_count -= line_count 

print("seniors list: ", seniors)
print("everyone else list: ", everyone_else)

#set the variables list item 0=name, 1=email address 2=atnum, 
# 3=skipnum, 4=attrate, 5=remaining_number of sessions, 6=passfail 7=still need to attend  8=email message
attrate = 0
remaining_number_sessions_seniors = 0
neednum_seniors = 0
neednum_everyone_else = 0
remaining_dates_seniors = [
'4-25', '4-26', '4-27', '4-28',
'5-2', '5-3', '5-4', '5-5'
]

remaining_number_sessions_seniors = len(remaining_dates_seniors)
remaining_dates_sessions_seniors_string=''
remaining_dates_sessions_seniors_string=''.join([str(item) + ", " for item in remaining_dates_seniors])
remaining_dates_sessions_seniors_string_stripped=remaining_dates_sessions_seniors_string[:-2]
0

remaining_dates_everyone_else = [
'4-25', '4-26', '4-27', '4-28',
'5-2', '5-3', '5-4', '5-5',
'5-9', '5-10', '5-11', '5-12',
'5-16', '5-17', '5-18', '5-19'
] 

remaining_number_sessions_non_seniors = len(remaining_dates_everyone_else)
remaining_dates_everyone_else_string=''
remaining_dates_everyone_else_string=''.join([str(item) + ", " for item in remaining_dates_everyone_else])
remaining_dates_everyone_else_string_stripped=remaining_dates_everyone_else_string[:-2]

# Step 1: process attendance data and insert attnum, skipnum, attrate,
# remaining_number_sessions_non_seniors, and neednum_everyone_else into list

for student in everyone_else:
    skipnum = 0
    attnum = 0
    for i in student:
        if i=="P":
            attnum = attnum+1
        elif i=="A":
            skipnum = skipnum+1
        i += i
    student.append(attnum)
    student.append(skipnum)
    attrate = ((attnum/(attnum+skipnum))*100)
    format_attrate = "{:.2f}".format(attrate)
    student.append(format_attrate)
    student.append(remaining_number_sessions_non_seniors)
# calculate the minimum needed sessions to pass with more than 50% attendance
    if int(float(format_attrate)) >= 50:
        passfail="passing"
        student.append(passfail)
    else:
        passfail="failing"
        student.append(passfail)

    neednum_everyone_else = remaining_number_sessions_non_seniors
    while (attnum+neednum_everyone_else)/(attnum+skipnum+remaining_number_sessions_non_seniors) >= 0.5:
        neednum_everyone_else = (int(neednum_everyone_else) - 1)
    else:
        student.append(neednum_everyone_else + 1)

    # delete the unneeded attendance records
    del student[2:]
    #compose custom email message

    entry = "Dear " + student[0].strip() + ",\n\nHello varsity walker. I'm coach Reitz' python3 attendancebot!\n\nYou are currently " + passfail + " Spring Fitness. \n\nYour current attendance rate is:" + str(attrate) + "%. (You have attended " + str(attnum) + " sessions, and have been absent for " + str(skipnum) + " sessions.)\n\nYou still need to attend at least " + str(neednum_everyone_else) + " practices of the remaining " + str(remaining_number_sessions_non_seniors) + " in the school year in order to reach the critical threshold of the majority of practices (i.e. an attendance rate of at least 50%) and pass Spring Fitness. \n\nYour remaining practice dates are: " + str(remaining_dates_everyone_else_string_stripped) + ". \n\nSincerely, \n Mr Coach's Python3 Attendance-bot \n\n"
    email_report = str(entry)
    #attach the email report to string
    student.append(email_report)

# Step 2: process attendance data for seniors and insert attnum, skipnum, attrate,  
# remaining_number_sessions_non_seniors, and neednum_everyone_else into list

for student in seniors:
    skipnum = 0
    attnum = 0
    for i in student:
        print([[i]])
        if i == "P":
            attnum = attnum + 1
        elif i == "A":
            skipnum = skipnum + 1
        i += i
    student.append(attnum)
    student.append(skipnum)
    attrate = ((attnum / (attnum + skipnum)) * 100)
    format_attrate = "{:.2f}".format(attrate)
    student.append(format_attrate)
    student.append(remaining_number_sessions_seniors)
    # calculate the minimum needed sessions to pass with more than 50% attendance
    if int(float(format_attrate)) >= 50:
        passfail = "passing"
        student.append(passfail)
    else:
        passfail = "not passing"
        student.append(passfail)

    neednum_seniors = remaining_number_sessions_seniors
    while neednum_seniors >= 0:
        if (attnum + neednum_seniors) / (attnum + skipnum + remaining_number_sessions_seniors) >= 0.5:
            student.append(neednum_seniors)
            break
        else:
            neednum_seniors = str(neednum_seniors - 1)

    if int(float(format_attrate)) >= 50:
        passfail="passing"
    else: 
        passfail="not passing"

    # delete the unneeded attendance records
    del student[2:]

    # calculate the minimum needed sessions to pass with more than 50% attendance
    neednum_seniors = remaining_number_sessions_seniors

    while (attnum+neednum_seniors)/(attnum+skipnum+remaining_number_sessions_seniors) >= 0.5:
        neednum_seniors = int(neednum_seniors - 1)
    else:
        student.append(neednum_seniors + 1)

    # delete the unneeded attendance records
    del student[2:]
    #compose custom email message
    entry = "Dear " + student[0].strip() + ",\n\nHello varsity walker. I'm coach Reitz' python3 attendancebot!\n\nYou are currently " + passfail + " Spring Fitness. \n\nYour current attendance rate is:" + str(attrate) + "%. (You have attended " + str(attnum) + " sessions, and have been absent for " + str(skipnum) + " sessions.)\n\nYou still need to attend at least " + str(neednum_seniors) + " practices of the remaining " + str(remaining_number_sessions_seniors) + " in the school year in order to reach the critical threshold of the majority of practices (i.e. an attendance rate of at least 50%) and pass Spring Fitness. \n\nYour remaining practice dates are: " + str(remaining_dates_sessions_seniors_string_stripped) + ". \n\nSincerely, \n Mr Coach's Python3 Attendance-bot \n\n"
    email_report = str(entry)
    student.append(email_report)

#email each student with customized email message
import smtplib, ssl

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()
    return user, passw

port = 465
sender, password = read_creds()

i_inner=[]
for student in everyone_else:
    for i_inner in student:
        print("And now we will prep to send the following message: \n")
        print(student[0])
        receive = student[1]
        print("sending to: ")
        print(receive)
        SUBJECT = "Spring Fitness Attendance Update"
        print(SUBJECT)
        TEXT = student[2]
        print(TEXT)

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        context = ssl.create_default_context()
        print("Starting to send to non-seniors")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
             server.login(sender, password)
             server.sendmail(sender, receive, message)
        print("sent emails to non-seniors!")
        break
#create a report.csv file of the new lists
Details = ['name', 'email', 'email']
with open('report.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(Details) 
    for item in everyone_else:
        write.writerow(item[0:2])
        print(item[0:2])
    for item in seniors:
        write.writerow(item[0:2])
        print(item[0:2])
    
i_inner=[]
for student in seniors:
    for element in student:
        receive = student[1]
        print(receive)
        SUBJECT = "Spring Fitness Attendance Update"
        TEXT = student[2]
        print(TEXT)
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        context = ssl.create_default_context()
        print("Starting to send to seniors")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
             server.login(sender, password)
             server.sendmail(sender, receive, message)
        print("sent emails to seniors!")
        break

    print(seniors)
    print("\n")
    print(everyone_else)
