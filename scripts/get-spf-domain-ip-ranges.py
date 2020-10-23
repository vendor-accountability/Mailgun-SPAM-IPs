#!/usr/bin/env python3

# We manually figure out in advance what domain(s) they use for SPF records if it's not the main one.

import sys
import re
from SPF2IP import SPF2IP

domain_name=sys.argv[1]

# Special case if ARGV1 ends in -spf.txt remove that
if re.search("-spf.txt$", domain_name):
    domain_name = re.sub("-spf.txt$", "", domain_name)

file_name=domain_name + "-spf.txt"

lookup = SPF2IP(domain_name)

IP_blocks=lookup.IPArray('4')

with open(file_name, 'w') as f:
    for item in IP_blocks:
        f.write("%s\n" % item)
