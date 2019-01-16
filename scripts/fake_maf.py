# Read inputs and write an maf file
# requires python3 because of StringIO
#
# Inputs: VCF file, reference file
# Output: MAF file

import argparse, sys, os
import pandas as pd
from uuid import uuid4
import hashlib, random
from io import StringIO

def main(args):
    m1 = md5checksum(args.vcf)
    sys.stderr.write("VCF MD5: "+m1+"\n")
    m3 = md5checksum(args.reference)
    sys.stderr.write("REFERENCE MD5: "+m3+"\n")
    of = open(args.output,'w')
    of.write(get_header()+"\n")
    of.write(get_lines(args.normal_name,args.tumor_name,args.variant_count))
    of.close()

def md5checksum(filename, block_size=2**20):
    md5 = hashlib.md5()
    fh = open(filename,'rb')
    while True:
        data = fh.read(block_size)
        if not data: break
        md5.update(data)
    fh.close()
    return md5.hexdigest()

def get_lines(tumor_name,normal_name,variant_count):
    # hardcoding in location of maf data
    maf = pd.read_csv('data/resource/downsampled_maf.tsv',sep="\t")
    maf['Tumor_Sample_Barcode'] = tumor_name
    maf['Matched_Norm_Sample_Barcode'] = normal_name
    maf = maf.sample(variant_count)
    sh = StringIO()
    maf.to_csv(sh,sep="\t",index=False)
    sh.seek(0)
    return str(sh.read())

def get_header():
    header='''#version 2.4'''
    return header

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--variant_count',type=int,default=10)
parser.add_argument('-o','--output',required=True)
parser.add_argument('vcf')
parser.add_argument('reference')
parser.add_argument('normal_name')
parser.add_argument('tumor_name')
args = parser.parse_args()



main(args)
