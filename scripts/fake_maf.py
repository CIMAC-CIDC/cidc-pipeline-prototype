# Read inputs and write an maf file
#
# Inputs: VCF file, reference file
# Output: MAF file

import argparse, sys, os
from uuid import uuid4
import hashlib, random
def main(args):
    m1 = md5checksum(args.vcf)
    sys.stderr.write("VCF MD5: "+m1+"\n")
    m3 = md5checksum(args.reference)
    sys.stderr.write("REFERENCE MD5: "+m3+"\n")
    of = open(args.output,'w')
    of.write(get_header()+"\n")
    for i in range(0,args.variant_count):
        of.write(get_line(args.normal_name,args.tumor_name)+"\n")
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

def get_line(normal_name,tumor_name):
    line = '''SAMD11
148398
.
GRCh37
chr1
938958
938958
+
Intron
SNP
C
C
A
novel

MYID
NORMAL
C
C















c.431-82C>A


ENST00000342066







SAMD11,intron_variant,,ENST00000341065,;SAMD11,intron_variant,,ENST00000342066,;SAMD11,intron_variant,,ENST00000420190,;SAMD11,intron_variant,,ENST00000616016,;SAMD11,intron_variant,,ENST00000616125,;SAMD11,intron_variant,,ENST00000617307,;SAMD11,intron_variant,,ENST00000618181,;SAMD11,intron_variant,,ENST00000618323,;SAMD11,intron_variant,,ENST00000618779,;SAMD11,intron_variant,,ENST00000620200,;SAMD11,intron_variant,,ENST00000622503,;SAMD11,downstream_gene_variant,,ENST00000437963,;SAMD11,upstream_gene_variant,,ENST00000455979,;SAMD11,upstream_gene_variant,,ENST00000478729,;SAMD11,upstream_gene_variant,,ENST00000464948,;SAMD11,upstream_gene_variant,,ENST00000466827,;SAMD11,upstream_gene_variant,,ENST00000474461,;
A
ENSG00000187634
ENST00000342066
Transcript
intron_variant








1
SAMD11
HGNC
HGNC:28706
protein_coding










5/13

















MODIFIER















.
GCG
.
.



















'''
    line = line.split('\n')
    line[15] = tumor_name
    line[16] = normal_name
    return("\t".join(line))

def get_header():
    header='''#version 2.4
Hugo_Symbol	Entrez_Gene_Id	Center	NCBI_Build	Chromosome	Start_Position	End_Position	Strand	Variant_Classification	Variant_Type	Reference_Allele	Tumor_Seq_Allele1	Tumor_Seq_Allele2	dbSNP_RS	dbSNP_Val_Status	Tumor_Sample_Barcode	Matched_Norm_Sample_Barcode	Match_Norm_Seq_Allele1	Match_Norm_Seq_Allele2	Tumor_Validation_Allele1	Tumor_Validation_Allele2	Match_Norm_Validation_Allele1	Match_Norm_Validation_Allele2	Verification_Status	Validation_Status	Mutation_Status	Sequencing_Phase	Sequence_Source	Validation_Method	Score	BAM_File	Sequencer	Tumor_Sample_UUID	Matched_Norm_Sample_UUID	HGVSc	HGVSp	HGVSp_Short	Transcript_ID	Exon_Number	t_depth	t_ref_count	t_alt_count	n_depth	n_ref_count	n_alt_count	all_effects	Allele	Gene	Feature	Feature_type	Consequence	cDNA_position	CDS_position	Protein_position	Amino_acids	Codons	Existing_variation	ALLELE_NUM	DISTANCE	STRAND_VEP	SYMBOL	SYMBOL_SOURCE	HGNC_ID	BIOTYPE	CANONICAL	CCDS	ENSP	SWISSPROT	TREMBL	UNIPARC	RefSeq	SIFT	PolyPhen	EXON	INTRON	DOMAINS	AF	AFR_AF	AMR_AF	ASN_AF	EAS_AF	EUR_AF	SAS_AF	AA_AF	EA_AF	CLIN_SIG	SOMATIC	PUBMED	MOTIF_NAME	MOTIF_POS	HIGH_INF_POS	MOTIF_SCORE_CHANGE	IMPACT	PICK	VARIANT_CLASS	TSL	HGVS_OFFSET	PHENO	MINIMISED	ExAC_AF	ExAC_AF_AFR	ExAC_AF_AMR	ExAC_AF_EAS	ExAC_AF_FIN	ExAC_AF_NFE	ExAC_AF_OTH	ExAC_AF_SAS	GENE_PHENO	FILTER	flanking_bps	variant_id	variant_qual	ExAC_AF_Adj	ExAC_AC_AN_Adj	ExAC_AC_AN	ExAC_AC_AN_AFR	ExAC_AC_AN_AMR	ExAC_AC_AN_EAS	ExAC_AC_AN_FIN	ExAC_AC_AN_NFE	ExAC_AC_AN_OTH	ExAC_AC_AN_SAS	ExAC_FILTER	gnomAD_AF	gnomAD_AFR_AF	gnomAD_AMR_AF	gnomAD_ASJ_AF	gnomAD_EAS_AF	gnomAD_FIN_AF	gnomAD_NFE_AF	gnomAD_OTH_AF	gnomAD_SAS_AF'''
    return header

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--variant_count',type=int,default=500)
parser.add_argument('-o','--output',required=True)
parser.add_argument('vcf')
parser.add_argument('reference')
parser.add_argument('normal_name')
parser.add_argument('tumor_name')
args = parser.parse_args()



main(args)
