#!/bin/python

fd=open('sans99_mapping.md', encoding='utf-8')
outfd=open('charslist.py', encoding='utf-8', mode='w')

process=0
print('#!/usr/bin/python3', file=outfd)
print('charslist = {', file=outfd)
for line in fd:
    if line.startswith("### CHARS_START"):
        process = 1
        continue
    if line.startswith("### CHARS_END"):
        break
    if process == 0:
        continue
    inchars = line[:5].strip()
    if inchars == '"':
        inchars = '\\"'
    elif inchars == '\\':
        inchars = '\\\\'
    incodes,outcodes,_,devna = line[6:].split('|')
    outcodes = outcodes.strip().split(',')
    outcodes_hex = "".join([f'\\u{i}' for i in outcodes])
    outcodes_uni = "".join([chr(int(i,16)) for i in outcodes])
    print (f'''  {'"' + inchars + '":':6s} {'"' + outcodes_hex + '",':40s}  #   {outcodes_uni}''', file=outfd)
print('}', file=outfd)
