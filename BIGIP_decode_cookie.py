#!/usr/bin/python3

# example string: BIGip<ervername>=110536896.20480.0000

import struct
import sys
import re

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} cookie")
    exit(1)

cookie = sys.argv[1]
print(f"\n[*] Cookie to decode: {cookie}\n")

(cookie_name, cookie_value) = cookie.split('=')

pool = re.search('^BIGipServer([.\w\.]*)', cookie_name)

if pool is None:
    print("Error: Cookie name does not match expected format.")
    exit(1)

(host, port, end) = cookie_value.split('.')

(a, b, c, d) = [i for i in struct.pack("<I", int(host))]

(e1, e2) = struct.pack("<H", int(port))
port = "0x%02X%02X" % (e1, e2)

print(f"[*] Pool name: {pool.group(1)}")
print(f"[*] Decoded IP and Port: {a}.{b}.{c}.{d}:{int(port, 16)}\n")
