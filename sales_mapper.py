#!/usr/bin/env python3
import sys

for line in sys.stdin:
    #remove leading whitespace
    line = line.strip()
    #split line into fields seperated by comma
    fields = line.split(",")
    country = fields[7]
    print('%s\t%s' % (country, 1))
    
