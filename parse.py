#!/usr/bin/env python
import sys
import csv
import subprocess

with open(sys.argv[1]) as f:
  for row in csv.reader(f):
    if(row[2] == "" or row[3] == "" or row[4] == ""):
        continue;
    command = "date --date=\"" + row[0] + "\" \"+%s\"";
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait();
    #os.system(command)
    print(output + ", " + row[1] + ", " + row[2] + ", " + row[3] + ", " + row[4] + "@");
