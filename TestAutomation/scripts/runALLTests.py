'''
Team Steve
Michael O'Cain
Connor Yates
Christopher Tucker
'''

import os
import subprocess
import shutil
import webbrowser

# Navigate to the reports folder and create a new reports.html
os.chdir("..")
os.chdir("reports")
r = open("reports.html", "w")
htmlOpen = "<html><title>GlucosioConverter.java Test</title><center><h1>GlucosioConverter.java Test</h1><style>table, th, td {text-align:center; border: 1px solid black;} th,td{padding: 15px} tr:hover {background-color: lightGray;}</style><head></head><body><table><tr><th>File</th><th>Test ID</th><th>Method</th><th>Parameter</th><th>Oracle</th><th>Output</th><th>Result</th></tr>"
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
    with open(i) as f:
        arguments = f.readlines()
        #print(arguments)
        os.chdir("..")
        os.chdir("project")
        os.chdir("src")
        test_args = 'java Steve_Driver' + ' ' + arguments[1].strip() + " " + arguments[2].strip()

        # Temp array stores pointers that point to arguments elements without spaces
        temp_array = []
        temp_array.append(arguments[1].strip())
        temp_array.append(arguments[2].strip())

        # Call Steve_Driver on command line
        subprocess.call('javac Steve_Driver.java', stdin=None, stdout=None, stderr=None, shell=True)
        p = subprocess.Popen('java Steve_Driver ' + temp_array[0] + ' ' + temp_array[1], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)

        os.chdir("..")
        os.chdir("..")
        os.chdir("reports")
        # i-name,arguments[0]-id,arguments[1]-method,arguments[2]-arg,arguments[3]-oracle
        # This loop prints the results of the driver
        output = p.stdout.read()
        if output.strip() == arguments[3].strip():
            #print("yes" + arguments[2] + " " + output)
            reportText = "<tr><td>" + i + "</td><td>" + arguments[0] + "</td><td>" + arguments[1] + "</td><td>" + arguments[2] + "</td><td>" + arguments[3] + "</td><td>" + output + "</td><td style='background-color:rgb(0, 255, 0);'>Pass</td></tr>"

        else:
            #print("fatality" + arguments[2] + " " + output)
            reportText = "<tr><td>" + i + "</td><td>" + arguments[0] + "</td><td>" + arguments[1] + "</td><td>" + arguments[2] + "</td><td>" + arguments[3] + "</td><td>" + output + "</td><td style='background-color:rgb(255, 0, 0);'>Fail</td></tr>"

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
