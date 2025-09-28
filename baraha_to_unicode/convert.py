#!/usr/bin/python3

import sys
import argparse
import logging
import re

E_MODIFIER = '\u093f'
HALF_MODIFIER = '\u094d'

CONSONANTS_CLASS=r'[\u0915-\u0939\u0958-\u095f]'
MATRAS_CLASS=r'[\u093e-\u094d]'
CAV_CLASS=r'[\u0901-\u0903]'  ## chandrabind+anuswara+visarga
SWARA_CLASS=r'[\u0951\u0952\u1cda]'
MATRAS_CAV_CLASS = r'[\u093e-\u094d\u0901-\u0903]'

try:
    from charslist import charslist
except ImportError:
    print (f"charslist.py missing. Please run prepare_chars_list.py first")
    exit(1)

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

def parse_args():
    parser = argparse.ArgumentParser(description='Sanskrit99 to Unicode Converter')
    parser.add_argument("-i", "--infile", help="input file", default="")
    parser.add_argument("-o", "--outfile", help="output file", default="")
    parser.add_argument("-d", "--debug", help="turn on debug prints", action="store_true")
    parser.add_argument("-l", "--logfile", help="debug log file", default="")
    parser.add_argument("-N", "--includenumbers", help="skip-numbers", action="store_true")
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

    global charslist
    if not cmd_options.includenumbers:
        numbers = { "0", "1", "2", "3", "4",
                    "5", "6", "7", "8", "9", }
        filtered_charlist = [ (i,j) for (i,j) in charslist if i not in numbers ]
        charslist = filtered_charlist

    return infd, outfd

def work_on_ematra(instr):
    ## work on the damn i's.
    ##   To match: i (consonant,HALF_MODIFIER)* consonant
    ##   To replace: (consonant,HALF_MODIFIER)* consonant E_MODIFIER
    outstr = ""
    state = "INIT"
    curr_consonant = ""
    for c in instr:
        if state == "INIT" and c != 'Ë':
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
                if c != 'Ë':
                    outstr += c
                    state = "INIT"
                else:
                    state = "I"
    return outstr

def convert(instr):

    ## the matras for the various -nga chars should come post the -nga char
    instr = re.sub(r'([ÆðÇÑÒÓÔÕÔÕÖ×ØÙÚÛÜãäåæç]*)¡',r'¡\1', instr)
    ## remove spaces after the E-matra
    instr = re.sub(r'([ËÌÍÎ])(\s+)',r'\1', instr)
    ## remove spaces before the matras
    instr = re.sub(r'\s+([ÅÆðÇÈ¡ÉÊÏÐÑÒÓÔÕÔÕÖ×ØÙÚÛÜãäåæç])', r'\1', instr)

    for lhs,rhs in charslist:
        instr = instr.replace(lhs, rhs)

    ## converge all E matra to one
    instr = re.sub(r'[ÌÍÎ]', 'Ë', instr)

    instr = work_on_ematra(instr)

    instr = re.sub(r'इïं', "ईं", instr)
    instr = re.sub(r'इï', "ई", instr)

    logging.debug("instr before r-conversion: %s", instr)

    ## put the ï before the consonant and its optional matras/cavs
    instr = re.sub(r''.join((r'(',CONSONANTS_CLASS,r')(',MATRAS_CAV_CLASS,r'*)ï')), r'ï\1\2' , instr)

    logging.debug("instr after bringing r before its consonant: %s", instr)
    ## put the ï before the half-consonants
    instr = re.sub(r''.join((r'((',CONSONANTS_CLASS,HALF_MODIFIER,r')+)ï')), r'ï\1' , instr)
    ## sub ï with half-r
    instr = re.sub(r'ï', "र्", instr)

    ## remove spaces before MATRAS_CAV_CLASS symbols
    instr = re.sub(r''.join((r'\s+(',MATRAS_CAV_CLASS,')')),r'\1', instr)
    ## CAV_CLASS should come after MATRAS_CLASS
    instr = re.sub(r''.join((r'(',CAV_CLASS,r')(',MATRAS_CLASS,r')')),r'\2\1', instr)
    ## SWARA_CLASS should come after MATRAS_CLASS, CAV_CLASS
    instr = re.sub(r''.join((r'(',SWARA_CLASS,r')(',MATRAS_CLASS,r')?(',CAV_CLASS,r')?')),r'\2\3\1', instr)

    return instr

def main():
    infd, outfd = parse_args()
    instr = infd.read()
    outstr = convert(instr)
    outfd.write(outstr)

main()

