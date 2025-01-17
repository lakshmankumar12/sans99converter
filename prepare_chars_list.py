#!/bin/python

fd=open('sans99_mapping.md', encoding='utf-8')
outfd=open('charslist.py', encoding='utf-8', mode='w')

process=0
print('#!/usr/bin/python3', file=outfd)
print('grand_chars_list = [', file=outfd)
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
    incodes,outcodes,state,devna = line[6:].split('|')
    outcodes = outcodes.strip().split(',')
    outcodes = "".join([f'\\u{i}' for i in outcodes])
    print (f'  [ "{inchars}", "{outcodes}", "{state.strip()}" ], # {devna.strip()}', file=outfd)
print(']', file=outfd)
