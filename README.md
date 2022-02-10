# CidrMerge
This was made to be a super simple script to merge connecting/congruent cidrs, and print them to the stdout. It only currently works with ipv4, i'll add ipv6 if needed or upon request. I also thought it would be a neat idea to regex all ips, and try to do the same thing.

## Usage

#### STDIN
```bash
echo "
192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24
" | cidrmerge

192.168.0.0/22
```

#### File/Arguments
```bash
./cidrmerge.py -f testfile
192.168.0.0/22
```

