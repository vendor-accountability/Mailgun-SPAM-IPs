#!/usr/bin/env python3

# Hardcoded to Mailgun for now

# Get list of network blocks

from SPF2IP import SPF2IP
lookup = SPF2IP('mailgun.org')

IP_blocks=lookup.IPArray('4')

with open('mailgun.org-spf.txt', 'w') as f:
    for item in IP_blocks:
        f.write("%s\n" % item)

# Convert Network blocks to IP_blocks and iterate over them with pydnsbl

from netaddr import IPNetwork
import pydnsbl

for entry in IP_blocks:
    for IP_address in IPNetwork(entry):
        print(IP_address)
        ip_checker = pydnsbl.DNSBLIpChecker()
        data=ip_checker.check(str(IP_address))
        print(data.detected_by)
        # put this data into a txt file in the file data/A/B/C/A.B.C.D
        # also run this in a multiprocessing pool
