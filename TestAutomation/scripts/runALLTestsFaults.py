'''
Team Steve
Michael O'Cain
Connor Yates
Christopher Tucker
'''

import os
import subprocess
import webbrowser
from datetime import datetime, date

# Navigate to the reports folder and create a new reports.html
os.chdir("..")
os.chdir("reports")
r = open("reports.html", "w")
htmlOpen = "<html><title>GlucosioConverterF.java Test</title><center><h1>GlucosioConverter.java Test</h1><style>table, th, td {text-align:center; border: 1px solid black;} th,td{padding: 15px} tr:hover {background-color: lightGray;}</style><head></head><body><table><tr><th>File</th><th>Test ID</th><th>Method</th><th>User Description</th><th>Parameter</th><th>Oracle</th><th>Output</th><th>Result</th><th>Date</th><th>Time</th></tr>"
htmlClose = "</table></body></center></html>"
r.write(htmlOpen)

os.chdir("..")
os.chdir("testCases")

# Stores all testCase files in the list "files_list"
files_list = []
for (dirpath, dirnames, filenames) in os.walk('.', topdown=False):
    files_list.extend(filenames)
    break

# Sorts the TestCase.txt files in numerical order
files_list = sorted(files_list)
#print(files_list)

# This loop gives the arguments in each TestCase.txt to the driver
for i in files_list:
    arguments = []
    # arguments[0] = Test ID
    # arguments[1] = Method being called (args[0] in Steve_Driver.java)
    # arguments[2] = Argument being passed into method call in driver (args[1] in Steve_Driver.java)
    # arguments[3] = Oracle

    with open(i) as f:
        arguments = f.readlines()
        #print(arguments)
        os.chdir("..")
        os.chdir("project")
        os.chdir("src")
        test_args = 'java Steve_DriverF' + ' ' + arguments[1].strip() + " " + arguments[2].strip()

        # Temp array stores pointers that point to arguments elements without spaces
        temp_array = []
        temp_array.append(arguments[1].strip())
        temp_array.append(arguments[2].strip())

        # Call Steve_Driver on command line
        subprocess.call('javac Steve_DriverF.java', stdin=None, stdout=None, stderr=None, shell=True)
        p = subprocess.Popen('java Steve_DriverF ' + temp_array[0] + ' ' + temp_array[1], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = str(date.today().strftime("%b-%d-%Y"))
        # Displays methods being completed in terminal
        print("Method: " + arguments[1].strip() + " Test ID: " + arguments[0].strip() + " Completed on " + current_date + " at " + current_time)
        #print("now = " + now)

        os.chdir("..")
        os.chdir("..")
        os.chdir("reports")


        # This loop prints the results of the driver
        output = p.stdout.read()
        if output.strip() == arguments[3].strip():
            #print("yes" + arguments[2] + " " + output)
            reportText = "<tr><td>" + i + "</td><td>" + arguments[0] + "</td><td>" + arguments[1] + "</td><td>" + arguments[4] + "</td><td>" + arguments[2] + "</td><td>" + arguments[3] + "</td><td>" + output + "</td><td style='background-color:rgb(0, 255, 0);'>Pass</td><td>" + current_date + "</td><td>" + current_time + "</td></tr>"

        else:
            #print("fatality" + arguments[2] + " " + output)
            reportText = "<tr><td>" + i + "</td><td>" + arguments[0] + "</td><td>" + arguments[1] + "</td><td>" + arguments[4] + "</td><td>" + arguments[2] + "</td><td>" + arguments[3] + "</td><td>" + output + "</td><td style='background-color:rgb(255, 0, 0);'>Fail</td><td>" + current_date + "</td><td>" + current_time + "</td></tr>"

        r.write(reportText)

        # Change directories back into the testCases folder
        os.chdir("..")
        os.chdir("testCases")

# Completes reports.html
r.write(htmlClose)

os.chdir("..")
os.chdir("reports")
#subprocess.call("ls")

# This gets reports.html file path
reportPath = os.path.abspath("reports.html")
#print(reportPath)

# open in a new tab, if possible
new = 2

# open a public URL, in this case, the webbrowser docs
url = reportPath
webbrowser.open(url, new=new)

# open an HTML file on Windows computer
'''
url = "file:/" + reportPath
webbrowser.open(url,new=new)
'''
