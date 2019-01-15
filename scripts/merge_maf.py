# Read inputs and write MAF
# 
# Inputs: list of maf files
# Output: merged maf file

import argparse, sys, os
from uuid import uuid4
import hashlib, random
def main(args):
    fh = open(args.vcfs[0],'rt')
    line1 = fh.readline()
    line2 = fh.readline()
    fh.close()
    of = open(args.output,'w')
    of.write(line1)
    of.write(line2)
    for file in args.vcfs:
        fh = open(file,'rt')
        temp1 = fh.readline()
        temp2 = fh.readline()
        for line in fh:
            of.write(line)
        fh.close()
    of.close()

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-o','--output',required=True)
parser.add_argument('vcfs',nargs='+')
args = parser.parse_args()



main(args)
