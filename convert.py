#!/usr/bin/python3

import sys
from enum import Enum
import argparse
import logging

try:
    from charslist import charslist
except ImportError:
    print (f"charslist.py missing. Please run prepare_chars_list.py first")
    exit(1)


E_MODIFIER = '\u093f'
HALF_MODIFIER = '\u094d'
HALF_RA = '\u0930' + HALF_MODIFIER

def parse_args():
    parser = argparse.ArgumentParser(description='Sanskrit99 to Unicode Converter')
    parser.add_argument("-i", "--infile", help="input file", default="")
    parser.add_argument("-o", "--outfile", help="output file", default="")
    parser.add_argument("-d", "--debug", help="turn on debug prints", action="store_true")
    parser.add_argument("-l", "--logfile", help="debug log file", default="")
    cmd_options = parser.parse_args()

    infd = sys.stdin
    outfd = sys.stdout
    if cmd_options.infile != "":
        infd = open(cmd_options.infile, 'r', encoding='utf-8')
    if cmd_options.outfile != "":
        outfd = open(cmd_options.outfile, 'w', encoding='utf-8')
    if cmd_options.debug:
        handlers=[
            (logging.FileHandler(cmd_options.logfile)
             if cmd_options.logfile
             else logging.StreamHandler(sys.stdout))
        ]
        logging.basicConfig(level=logging.DEBUG,
              format='%(asctime)s - %(levelname)s - %(message)s',
              handlers=handlers)

    return infd, outfd

def is_consonant(c):
    ## plain consonant between क and ह
    return '\u0915' <= c <= '\u0939'

def is_vowel_modifier(c):
    ## between ा and ौ
    return '\u093e' <= c <= '\u094c'

def is_modifier2(c):
    return c in "\u0902\u0903"

def is_modifier3(c):
    return c in "\u0951\u0952\u1cda"

def convert_current_buffer(buf):
    for i in range(len(buf),0,-1):
        inchar = buf[:i]
        logging.debug (f"Evaluating inchar: {inchar}, i:{i}")
        if inchar in charslist:
            logging.debug (f"Got match: {charslist[inchar]}. Left:{buf[i:]}")
            return charslist[inchar], buf[i:]
    ## no match. Just remove last and give as is
    return buf[0], buf[1:]

def work_on_ematra(instr):
    ## work on the damn i's.
    ##   To match: i (consonant,HALF_MODIFIER)* consonant
    ##   To replace: (consonant,HALF_MODIFIER)* consonant E_MODIFIER
    outstr = ""
    state = "INIT"
    curr_consonant = ""
    for c in instr:
        if state == "INIT" and c != 'i':
            outstr += c
        elif state == "INIT":
            ## c==i
            state = "I"
            curr_consonant = ""
        elif state == "I":
            if is_consonant(c):
                state = "I_AND_CONS"
                curr_consonant = c
            elif is_modifier3(c):
                ## accept this and be in same state
                outstr += c
            else:
                ## error. keep i in and move on.
                outstr += E_MODIFIER
                state = "INIT"
        else:
            ## state == "I_AND_CONS"
            if c == HALF_MODIFIER:
                outstr += curr_consonant + c
                state = "I"
            else:
                outstr += curr_consonant + E_MODIFIER
                ## mind you the c can be another i!
                if c != 'i':
                    outstr += c
                    state = "INIT"
                else:
                    state = "I"
    return outstr

def work_on_Rs(instr):
    ## work on the damn i's.
    ##   To match:   (consonant,HALF_MODIFIER)* consonant (VOWELIZER)? R
    ##   To replace: HALF_RA, HALF_MODIFIER, (consonant,HALF_MODIFIER)* consonant (VOWELIZER)
    outstr = ""
    state = "INIT"
    curr_capture = ""
    for c in instr:
        if c != "R":
            outstr += c
            continue
        curr_capture = ""
        outstr, lastc = outstr[:-1], outstr[-1]
        if is_modifier3(lastc):
            curr_capture = lastc + curr_capture
            outstr, lastc = outstr[:-1], outstr[-1]
        if is_modifier2(lastc):
            curr_capture = lastc + curr_capture
            outstr, lastc = outstr[:-1], outstr[-1]
        if is_vowel_modifier(lastc):
            curr_capture = lastc + curr_capture
            outstr, lastc = outstr[:-1], outstr[-1]
        while True:
            curr_capture = lastc + curr_capture
            outstr, lastc = outstr[:-1], outstr[-1]
            if lastc == HALF_MODIFIER:
                curr_capture = lastc + curr_capture
                outstr, lastc = outstr[:-1], outstr[-1]
                continue
            ## put the HALF_RA here
            outstr += lastc + HALF_RA + curr_capture
            break
        curr_capture = ""
    return outstr

def convert(instr):
    ## first convert all chars in order
    outstr = ""
    currbuf = ""
    for c in instr:
        currbuf += c
        logging.debug (f"currbuf: {currbuf}, char: {c}")
        if len(currbuf) < 3:
            continue
        outchar, currbuf = convert_current_buffer(currbuf)
        outstr += outchar
        logging.debug (f"outstr: {outstr}")
    while currbuf:
        outchar, currbuf = convert_current_buffer(currbuf)
        outstr += outchar

    outstr = outstr.replace('¡', 'R\u0902')

    outstr = work_on_ematra(outstr)
    outstr = work_on_Rs(outstr)

    return outstr

def main():
    infd, outfd = parse_args()
    instr = infd.read()
    outstr = convert(instr)
    outfd.write(outstr)


main()

