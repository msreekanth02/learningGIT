Directories
===========
import os
os.listdir("/Users/I543801")
dir = "/Users/I543801"
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
         print("{} is a directory",.format(fullname))
    else:
         print("{} is a file".format(fullname))

CSV Reader
==========
$ touch csv_file.txt "create a file with comma saparator"
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

Generating CSV File
====================
hosts = [["workstation.local", "192.168.1.23"], ["webserver.cloud", "10.2.3.5"]]
with open("hosts.csv", 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

$cat hosts.csv

Reading and writing CSV files thru Dictionaries
===============================================