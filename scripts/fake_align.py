import argparse, sys, os
from uuid import uuid4
import hashlib, random
from subprocess import Popen, PIPE

def main(args):
    os.chdir(args.cwd)
    header = get_header()
    m1 = md5checksum(args.fq1)
    sys.stderr.write("FASTQ1 MD5: "+m1+"\n")
    m2 = md5checksum(args.fq2)
    sys.stderr.write("FASTQ2 MD5: "+m2+"\n")
    m3 = md5checksum(args.reference)
    sys.stderr.write("REFERENCE MD5: "+m3+"\n")
    stream = Popen(['samtools','view','-Sb','-','-o',args.output],stdin=PIPE)
    stream.stdin.write(header+"\n")
    for i in range(0,args.alignment_count):
        stream.stdin.write(get_line()+"\n")
    stream.communicate()

def md5checksum(filename, block_size=2**20):
    md5 = hashlib.md5()
    fh = open(filename,'rb')
    while True:
        data = fh.read(block_size)
        if not data: break
        md5.update(data)
    fh.close()
    return md5.hexdigest()

def get_line():
    return str(uuid4())+"	77	*	0	0	*	*	0	0	"+'N'*76+"	"+'#'*76+"	AS:i:0	XS:i:0"

def get_header():
    header = '''@SQ	SN:chr1	LN:248956422
@SQ	SN:chr10	LN:133797422
@SQ	SN:chr11	LN:135086622
@SQ	SN:chr12	LN:133275309
@SQ	SN:chr13	LN:114364328
@SQ	SN:chr14	LN:107043718
@SQ	SN:chr15	LN:101991189
@SQ	SN:chr16	LN:90338345
@SQ	SN:chr17	LN:83257441
@SQ	SN:chr18	LN:80373285
@SQ	SN:chr19	LN:58617616
@SQ	SN:chr2	LN:242193529
@SQ	SN:chr20	LN:64444167
@SQ	SN:chr21	LN:46709983
@SQ	SN:chr22	LN:50818468
@SQ	SN:chr3	LN:198295559
@SQ	SN:chr4	LN:190214555
@SQ	SN:chr5	LN:181538259
@SQ	SN:chr6	LN:170805979
@SQ	SN:chr7	LN:159345973
@SQ	SN:chr8	LN:145138636
@SQ	SN:chr9	LN:138394717
@SQ	SN:chrM	LN:16569
@SQ	SN:chrX	LN:156040895
@SQ	SN:chrY	LN:57227415
@PG	ID:bwa	PN:bwa	VN:0.7.15-r1140	CL:bwa mem -t 24 -a -M /Reference/Human/hg38/Indecies/hg38.canonical.bwa/hg38.canonical.bwa /dev/fd/63 /dev/fd/62'''
    return header

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--alignment_count',type=int,default=100)
parser.add_argument('-o','--output',required=True)
parser.add_argument('fq1')
parser.add_argument('fq2')
parser.add_argument('reference')
parser.add_argument('cwd')
args = parser.parse_args()

main(args)
