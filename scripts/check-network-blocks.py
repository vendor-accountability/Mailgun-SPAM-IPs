#!/usr/bin/env python3

import sys
from netaddr import IPNetwork
import threading
import queue
import pydnsbl
import time
import os
import json

# Get list of network blocks from file

file_name=sys.argv[1]

# Copied from https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file

# The queue for tasks
q = queue.Queue()

# Worker, handles each task
def worker():
    while True:
        item = q.get()
        if item is None:
            break
        IP_octets=item.split(".")
        ip_checker = pydnsbl.DNSBLIpChecker()
        data=ip_checker.check(item)
        output_dir="data/" + IP_octets[0] + "/" + IP_octets[1] + "/" + IP_octets[2]
        os.makedirs(output_dir, exist_ok = True)
        output_file="data/" + IP_octets[0] + "/" + IP_octets[1] + "/" + IP_octets[2] + "/" + item + ".txt"
        # Write output details to file in JSON format
        # write them all so we know for sure that it got checked, also no logic for state changes is needed as we log all state changes
        with open(output_file, 'w') as f:
            f.write(json.dumps(data.detected_by))
        print(item)
        q.task_done()

# Notes on worker_pool size: 100 breaks with OSErr to many open files in default windows containers and 50 seems safe

def start_workers(worker_pool=10):
    threads = []
    for i in range(worker_pool):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)
    return threads


def stop_workers(threads):
    # stop workers
    for i in threads:
        q.put(None)
    for t in threads:
        t.join()


def create_queue():
    with open(file_name, 'r') as f:
        for line in f:
            # Read each network block and convert to a list of IPs, convert that to a string and feed it into the queue
            for IP_address in IPNetwork(line):
                IP_address=str(IP_address)
                q.put(IP_address)

if __name__ == "__main__":
    # Start up your workers
    workers = start_workers()

    # Call queue creation which includes feeding the file specified in ARGV1
    create_queue()

    # Blocks until all tasks are complete
    q.join()

    stop_workers(workers)
