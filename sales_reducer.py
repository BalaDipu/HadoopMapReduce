#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_country = None
current_count = 0
country = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    country, count = line.split('\t')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_country == country:
        current_count += count
    else:
        if current_country:
            # write result to STDOUT
            print('%s\t%s' % (current_country, current_count))
        current_count = count
        current_country = country

# do not forget to output the last country if needed!
if current_country == country:
    print('%s\t%s' % (current_country, current_count))
