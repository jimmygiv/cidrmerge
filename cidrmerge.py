#!/usr/bin/env python3
from netaddr import cidr_merge
from argparse import ArgumentParser
from re import findall,match,compile as recompile
from sys import stdin
from os import path

cidrre=recompile(r'((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9])))')
parser = ArgumentParser()
parser.add_argument("-f", type=str, required=True, help="file with cidrs")

if not stdin.isatty():
  text = stdin.read().strip()
else:
  args = parser.parse_args()
  if not path.isfile(args.f):
    print("[!] No such file or directory")
    exit()
  else:
    text = open(args.f, 'r').read().strip()


#grab cidrs
nets = []
for line in findall(cidrre, text):
  if match(cidrre, line[0]):
    nets.append(line[0])

#dedup & merge
netranges = cidr_merge(nets)


print('\n'.join(str(v) for v in netranges))

