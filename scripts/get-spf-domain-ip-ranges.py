#!/usr/bin/env python3

# Hardcoded to Mailgun for now

# Get list of network blocks

# will need to talk just a domain name, we'll manually figure out in advance what domain(s) they use for SPF records if it's not the main one.

from SPF2IP import SPF2IP
lookup = SPF2IP('mailgun.org')

IP_blocks=lookup.IPArray('4')

with open('mailgun.org-spf.txt', 'w') as f:
    for item in IP_blocks:
        f.write("%s\n" % item)
