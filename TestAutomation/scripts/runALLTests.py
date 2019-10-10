'''
Team Steve
Michael O'Cain
Connor Yates
Christopher Tucker
'''

import os
import subprocess
import shutil


t_list = []

t = open("testCase1.txt", "w+")

subprocess.call('javac Driver.java', stdin=None, stdout=None, stderr=None, shell=True)
subprocess.call('java Driver 10.04 1', stdin=None, stdout=t, stderr=None, shell=True)

subprocess.call('javac Driver.java', stdin=None, stdout=None, stderr=None, shell=True)
subprocess.call('java Driver 10.04 a', stdin=None, stdout=t, stderr=None, shell=True)

subprocess.call('javac Driver.java', stdin=None, stdout=None, stderr=None, shell=True)
subprocess.call('java Driver b 2', stdin=None, stdout=t, stderr=None, shell=True)

subprocess.call('javac Driver.java', stdin=None, stdout=None, stderr=None, shell=True)
subprocess.call('java Driver -1 1', stdin=None, stdout=t, stderr=None, shell=True)

subprocess.call('javac Driver.java', stdin=None, stdout=None, stderr=None, shell=True)
subprocess.call('java Driver 10.04 -1', stdin=None, stdout=t, stderr=None, shell=True)

# Copies test results into a list
with open('testCase1.txt', 'r') as f:
    t_list = f.readlines()

t.close()

os.chdir("..")
os.chdir("reports")

r = open("report.txt", "w+")

r.write('This is the report for the tests of the method\n')
r.write('"public static double round(double value, int places)" in the\n')
r.write('java class "public final class GlucosioConverter"\n')
r.write("\n")

r.write("Test one: args[0] = 10.04, args[1] = 1.\n")
r.write("The expected outcome was: 10.0\n")
r.write("The actual outcome was: ")
r.write(str(t_list[0]))
r.write("\n")

r.write("Test two: args[0] = 10.04, args[1] = a.\n")
r.write("The expected outcome was: Error\n")
r.write("The actual outcome was: ")
r.write(str(t_list[1]))
r.write("\n")

r.write("Test three: args[0] = b, args[1] = 2.\n")
r.write("The expected outcome was: Error\n")
r.write("The actual outcome was: ")
r.write(str(t_list[2]))
r.write("\n")

r.write("Test four: args[0] = -1, args[1] = 1.\n")
r.write("The expected outcome was: -1.0\n")
r.write("The actual outcome was: ")
r.write(str(t_list[3]))
r.write("\n")

r.write("Test five: args[0] = 10.04, args[1] = -1.\n")
r.write("The expected outcome was: Error\n")
r.write("The actual outcome was: ")
r.write(str(t_list[4]))
r.write("\n")

r.close()

'''

def wrapStringInHTMLWindows(program, url, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = program + '.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()

    open_new_tab(filename)


'''

