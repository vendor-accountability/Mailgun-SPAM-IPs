# Vendor-SPAM-IPs

This is a list of vendors that primarily specialize in sending email as a service (e.g. Mailgun, SendGrid) and the "spaminess" of their IPs according to various lists.

The structure is "/vendor name/" with a file inside listing their domain(s), domain-spf.txt with the SPF data for each domain(s) and a "/vendor name/data/" directory with sub directories in the form "/vendor name/data/A/B/C/" (first, second and third octet of the IPv4 address) with a file for each IP at "/vendor name/data/A/B/C/A.B.C.D.txt" containing the data.

We do not currently support IPv6 (and in fairness I haven't seen any IPv6 records in SPF records yet, please let me know if you are aware of an email as a service provider using IPv6 with SPF). 

## Example: Mailgun

Mailgun appears to use mailgun.org for their SPF record for their IPs:

mailgun.org.            266     IN      TXT     "v=spf1 include:spf1.mailgun.org include:spf2.mailgun.org -all"

Note the -all, good to see.
