#!/usr/bin/env python

# Written by 0xmani
# [+]Usage: python jwt_cracker.py <token> <wordlist>

import sys
import base64
import hashlib
import hmac
import time
import multiprocessing


def bg_green(text):
    return '\033[42m' + text + '\033[0m'


def bold(text):
    return '\033[1m' + text + '\033[22m'


def red(text):
    return '\033[31m' + text + '\033[0m'


jwt = sys.argv[1]
wordlist_file = sys.argv[2]

if len(sys.argv) != 3:
    print("\nError: Missing Arguments")
    print("[+] Usage: python jwt_cracker.py <token> <wordlist>")
    sys.exit()

wordlist = []
try:
    with open(wordlist_file, 'r', encoding='latin-1') as f:
        wordlist = [line.strip() for line in f]
except FileNotFoundError:
    print("\n[-] Invalid File!")
    print("[-] Check the File Name and Path")
    sys.exit()

def sig(payload, secret):
    return base64.urlsafe_b64encode(hmac.new(secret.encode(), payload.encode(), hashlib.sha256).digest()).rstrip(b'=').decode()

def crack_secret(wordlist_chunk):
    header, payload, sign = jwt.split('.')
    for secret_key in wordlist_chunk:
        if sig('.'.join([header, payload]), secret_key) == sign:
            return secret_key
    return None

#print("\nStarting JWT_Cracker......")
starting_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
print(f"\nStarting JWT_Cracker at {bold(starting_time)}")


num_processes = multiprocessing.cpu_count()  # Number of processes to run in parallel
chunk_size = (len(wordlist) + num_processes - 1) // num_processes
secret_key = None

# Start time for progress indicator
start_time = time.time()

# Create and start processes
processes = []
for i in range(num_processes):
    start_idx = i * chunk_size
    end_idx = (i + 1) * chunk_size
    process = multiprocessing.Process(target=crack_secret, args=(wordlist[start_idx:end_idx],))
    processes.append(process)
    process.start()

# Wait for processes to finish
for process in processes:
    process.join()

# Calculate elapsed time
elapsed_time = time.time() - start_time

if secret_key:
    print("\n")
    print(f"\n\nElapsed Time: {elapsed_time:.2f} seconds")
    print("\n\n")
    print(f"Secret Key Found: {bg_green(secret_key)}")
else:
    print(f"\n\nElapsed Time: {elapsed_time:.2f} seconds")
    print("\nNo Secret Key Found :(")
    print("Check the Token you Entered.")
