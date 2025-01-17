#!/usr/bin/python

from enum import Enum
import argparse

from charslist import grand_chars_list

class States(Enum):
    S_EMP,
    S_VWL,
    S_VWLMOD2,
    S_HLFMORE,
    S_PLNCONS
    S_CONMOD1,
    S_CONMOD2,
    S_IWAIT,
    S_HLFMORE_AND_I,

class LetterTypes(Enum):
    VWL,
    MOD1,
    MOD2,
    MOD3,
    SINC,
    CMBC,
    HLFC,
    VWLC,
    INDP,
    SYMI,
    SYMR,
    SPECIAL1,

def parse_args():
    parser = argparse.ArgumentParser(description='Sanskrit99 to Unicode Converter')
    parser.add_argument("-i", "--infile", help="input file")
    parser.add_argument("-o", "--outfile", help="output file")
    cmd_options = parser.parse_args()
    return cmd_options

def get_char_from_file(infd):
    while True:
        char = infd.read(1)
        if not char:
            break
        yield ord(char)

def convert(infd, outfd, charlist):
    curr_in_buffer = ""
    for c in get_char_from_file(infd)
        if len(curr_in_buffer) < 3:
            curr_in_buffer += c
            continue
        s99char = None
        for i in [3,2,1]:
            s99char,i = charlist.get(curr_in_buffer, None)
            if s99char is not None:
                break
        if s99char is None:
            print (f"Error: No match for {curr_in_buffer}")
            exit(1)
        curr_in_buffer = curr_in_buffer[i:]
        process_s99char(s99char)


def process_s99char(inchar):


−



