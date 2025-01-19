#!/usr/bin/python3

fd=open('mapping.md', encoding='utf-8')
outfd=open('charslist.py', encoding='utf-8', mode='w')

process=0
print('#!/usr/bin/python3', file=outfd)
print('charslist = (', file=outfd)
for line in fd:
    if line.startswith("### CHARS_START"):
        process = 1
        continue
    if line.startswith("### CHARS_END"):
        break
    if process == 0:
        continue
    lhs, rhs, _ = line.split('|',2)
    lhs = lhs.strip()
    rhs = rhs.strip()
    if lhs:
        lhscodes = [int(i,16) for i in lhs.strip().split(',')]
    else:
        lhscodes = []
    if rhs:
        rhscodes = [int(i,16) for i in rhs.strip().split(',')]
    else:
        rhscodes = []
    lhscodestr = ''.join([f'\\u{i:04x}' for i in lhscodes])
    rhscodestr = ''.join([f'\\u{i:04x}' for i in rhscodes])
    lhsstr = ''.join([chr(i) for i in lhscodes])
    rhsstr = ''.join([chr(i) for i in rhscodes])
    print (f'''  ( {'"' + lhscodestr + '",':20s} {'"' + rhscodestr + '"),':35s} #  | {lhsstr:10s} | {rhsstr}''', file=outfd)
print(')', file=outfd)
