import argparse, sys, os
from uuid import uuid4
import hashlib, random
def main(args):
    m1 = md5checksum(args.normal_bam)
    sys.stderr.write("FASTQ1 MD5: "+m1+"\n")
    m2 = md5checksum(args.tumor_bam)
    sys.stderr.write("FASTQ2 MD5: "+m2+"\n")
    m3 = md5checksum(args.reference)
    sys.stderr.write("REFERENCE MD5: "+m3+"\n")
    of = open(args.output,'w')
    of.write(get_header()+"\n")
    for i in range(0,args.variant_count):
        of.write(get_line()+"\n")
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

def get_line():
    line = '''chr20	1234567	.	T	C	.	artifact_in_normal;mapping_quality;t_lod	DP=50;ECNT=1;NLOD=3.66;N_ART_LOD=3.33;POP_AF=0.001;P_GERMLINE=-3.036;TLOD=3.33	GT:AD:AF:F1R2:F2R1:MBQ:MFRL:MMQ:MPOS:OBAM:OBAMRC	0/0:43,4:0.122:27,1:16,3:21:192,199:21:20:false:false'''
    return line

def get_header():
    header='''##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##FILTER=<ID=artifact_in_normal,Description="artifact_in_normal">
##FILTER=<ID=base_quality,Description="alt median base quality">
##FILTER=<ID=clustered_events,Description="Clustered events observed in the tumor">
##FILTER=<ID=contamination,Description="contamination">
##FILTER=<ID=duplicate_evidence,Description="evidence for alt allele is overrepresented by apparent duplicates">
##FILTER=<ID=fragment_length,Description="abs(ref - alt) median fragment length">
##FILTER=<ID=germline_risk,Description="Evidence indicates this site is germline, not somatic">
##FILTER=<ID=mapping_quality,Description="ref - alt median mapping quality">
##FILTER=<ID=multiallelic,Description="Site filtered because too many alt alleles pass tumor LOD">
##FILTER=<ID=orientation_bias,Description="Orientation bias (in one of the specified artifact mode(s) or complement) seen in one or more samples.">
##FILTER=<ID=panel_of_normals,Description="Blacklisted site in panel of normals">
##FILTER=<ID=read_position,Description="median distance of alt variants from end of reads">
##FILTER=<ID=str_contraction,Description="Site filtered due to contraction of short tandem repeat region">
##FILTER=<ID=strand_artifact,Description="Evidence for alt allele comes from one read direction only">
##FILTER=<ID=t_lod,Description="Tumor does not meet likelihood threshold">
##FORMAT=<ID=AD,Number=R,Type=Integer,Description="Allelic depths for the ref and alt alleles in the order listed">
##FORMAT=<ID=AF,Number=A,Type=Float,Description="Allele fractions of alternate alleles in the tumor">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth (reads with MQ=255 or with bad mates are filtered)">
##FORMAT=<ID=F1R2,Number=R,Type=Integer,Description="Count of reads in F1R2 pair orientation supporting each allele">
##FORMAT=<ID=F2R1,Number=R,Type=Integer,Description="Count of reads in F2R1 pair orientation supporting each allele">
##FORMAT=<ID=FT,Number=1,Type=String,Description="Genotype-level filter">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=MBQ,Number=A,Type=Integer,Description="median base quality">
##FORMAT=<ID=MFRL,Number=R,Type=Integer,Description="median fragment length">
##FORMAT=<ID=MMQ,Number=A,Type=Integer,Description="median mapping quality">
##FORMAT=<ID=MPOS,Number=A,Type=Integer,Description="median distance from end of read">
##FORMAT=<ID=OBAM,Number=A,Type=String,Description="Whether the variant can be one of the given REF/ALT artifact modes.">
##FORMAT=<ID=OBAMRC,Number=A,Type=String,Description="Whether the variant can be one of the given REF/ALT artifact mode complements.">
##FORMAT=<ID=OBF,Number=A,Type=Float,Description="Fraction of alt reads indicating orientation bias error (taking into account artifact mode complement).">
##FORMAT=<ID=OBP,Number=A,Type=Float,Description="Orientation bias p value for the given REF/ALT artifact or its complement.">
##FORMAT=<ID=OBQ,Number=A,Type=Float,Description="Measure (across entire bam file) of orientation bias for a given REF/ALT error.">
##FORMAT=<ID=OBQRC,Number=A,Type=Float,Description="Measure (across entire bam file) of orientation bias for the complement of a given REF/ALT error.">
##FORMAT=<ID=PGT,Number=1,Type=String,Description="Physical phasing haplotype information, describing how the alternate alleles are phased in relation to one another">
##FORMAT=<ID=PID,Number=1,Type=String,Description="Physical phasing ID information, where each unique ID within a given sample (but not across samples) connects records within a phasing group">
##FORMAT=<ID=PL,Number=G,Type=Integer,Description="Normalized, Phred-scaled likelihoods for genotypes as defined in the VCF specification">
##FORMAT=<ID=SA_MAP_AF,Number=3,Type=Float,Description="MAP estimates of allele fraction given z">
##FORMAT=<ID=SA_POST_PROB,Number=3,Type=Float,Description="posterior probabilities of the presence of strand artifact">
##GATKCommandLine=<ID=FilterMutectCalls,CommandLine="FilterMutectCalls  --output filtered.vcf --variant /file.vcf  --log-somatic-prior -6.0 --tumor-lod 5.3 --normal-artifact-lod 0.0 --max-germline-posterior 0.025 --max-alt-allele-count 1 --min-median-mapping-quality 30 --min-median-base-quality 20 --max-median-fragment-length-difference 10000 --min-median-read-position 5 --max-events-in-region 2 --max-strand-artifact-probability 0.99 --min-strand-artifact-allele-fraction 0.01 --max-contamination-probability 0.1 --unique-alt-read-count 0 --dont-trim-active-regions false --max-disc-ar-extension 25 --max-gga-ar-extension 300 --padding-around-indels 150 --padding-around-snps 20 --kmer-size 10 --kmer-size 25 --dont-increase-kmer-sizes-for-cycles false --allow-non-unique-kmers-in-ref false --num-pruning-samples 1 --recover-dangling-heads false --do-not-recover-dangling-branches false --min-dangling-branch-length 4 --consensus false --max-num-haplotypes-in-population 128 --error-correct-kmers false --min-pruning 2 --debug-graph-transformations false --kmer-length-for-read-error-correction 25 --min-observations-for-kmer-to-be-solid 20 --likelihood-calculation-engine PairHMM --base-quality-score-threshold 18 --pair-hmm-gap-continuation-penalty 10 --pair-hmm-implementation FASTEST_AVAILABLE --pcr-indel-model CONSERVATIVE --phred-scaled-global-read-mismapping-rate 45 --native-pair-hmm-threads 4 --native-pair-hmm-use-double-precision false --debug false --use-filtered-reads-for-annotations false --bam-writer-type CALLED_HAPLOTYPES --dont-use-soft-clipped-bases false --capture-assembly-failure-bam false --error-correct-reads false --do-not-run-physical-phasing false --min-base-quality-score 10 --smith-waterman JAVA --use-new-qual-calculator false --annotate-with-num-discovered-alleles false --heterozygosity 0.001 --indel-heterozygosity 1.25E-4 --heterozygosity-stdev 0.01 --standard-min-confidence-threshold-for-calling 10.0 --max-alternate-alleles 6 --max-genotype-count 1024 --sample-ploidy 2 --genotyping-mode DISCOVERY --contamination-fraction-to-filter 0.0 --output-mode EMIT_VARIANTS_ONLY --all-site-pls false --interval-set-rule UNION --interval-padding 0 --interval-exclusion-padding 0 --interval-merging-rule ALL --read-validation-stringency SILENT --seconds-between-progress-updates 10.0 --disable-sequence-dictionary-validation false --create-output-bam-index true --create-output-bam-md5 false --create-output-variant-index true --create-output-variant-md5 false --lenient false --add-output-sam-program-record true --add-output-vcf-command-line true --cloud-prefetch-buffer 40 --cloud-index-prefetch-buffer -1 --disable-bam-index-caching false --help false --version false --showHidden false --verbosity INFO --QUIET false --use-jdk-deflater false --use-jdk-inflater false --gcs-max-retries 20 --disable-tool-default-read-filters false",Version=4.0.2.1,Date="March 12, 2018 5:02:42 AM UTC">
##GATKCommandLine=<ID=Mutect2,CommandLine="Mutect2  --tumor-sample 1 --normal-sample 1 --germline-resource /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-0/inputs/cluster/cidc/WDLExampleData/TESTREF20180211/Resources/af-only-gnomad.hg38.chr20chr21chrMchrY.vcf.gz --native-pair-hmm-threads 8 --output output.vcf --input /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-0/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-get_tumor/shard-0/execution/chr20.bam --input /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-0/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-get_normal/shard-0/execution/chr20.bam --reference /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-0/inputs/cluster/cidc/WDLExampleData/TESTREF20180211/chr20chr21chrYchrM.fa  --genotype-pon-sites false --af-of-alleles-not-in-resource 0.001 --log-somatic-prior -6.0 --tumor-lod-to-emit 3.0 --initial-tumor-lod 2.0 --max-population-af 0.01 --downsampling-stride 1 --max-suspicious-reads-per-alignment-start 0 --normal-lod 2.2 --annotation-group StandardMutectAnnotation --disable-tool-default-annotations false --dont-trim-active-regions false --max-disc-ar-extension 25 --max-gga-ar-extension 300 --padding-around-indels 150 --padding-around-snps 20 --kmer-size 10 --kmer-size 25 --dont-increase-kmer-sizes-for-cycles false --allow-non-unique-kmers-in-ref false --num-pruning-samples 1 --recover-dangling-heads false --do-not-recover-dangling-branches false --min-dangling-branch-length 4 --consensus false --max-num-haplotypes-in-population 128 --error-correct-kmers false --min-pruning 2 --debug-graph-transformations false --kmer-length-for-read-error-correction 25 --min-observations-for-kmer-to-be-solid 20 --likelihood-calculation-engine PairHMM --base-quality-score-threshold 18 --pair-hmm-gap-continuation-penalty 10 --pair-hmm-implementation FASTEST_AVAILABLE --pcr-indel-model CONSERVATIVE --phred-scaled-global-read-mismapping-rate 45 --native-pair-hmm-use-double-precision false --debug false --use-filtered-reads-for-annotations false --bam-writer-type CALLED_HAPLOTYPES --dont-use-soft-clipped-bases false --capture-assembly-failure-bam false --error-correct-reads false --do-not-run-physical-phasing false --min-base-quality-score 10 --smith-waterman JAVA --use-new-qual-calculator false --annotate-with-num-discovered-alleles false --heterozygosity 0.001 --indel-heterozygosity 1.25E-4 --heterozygosity-stdev 0.01 --standard-min-confidence-threshold-for-calling 10.0 --max-alternate-alleles 6 --max-genotype-count 1024 --sample-ploidy 2 --genotyping-mode DISCOVERY --contamination-fraction-to-filter 0.0 --output-mode EMIT_VARIANTS_ONLY --all-site-pls false --min-assembly-region-size 50 --max-assembly-region-size 300 --assembly-region-padding 100 --max-reads-per-alignment-start 50 --active-probability-threshold 0.002 --max-prob-propagation-distance 50 --interval-set-rule UNION --interval-padding 0 --interval-exclusion-padding 0 --interval-merging-rule ALL --read-validation-stringency SILENT --seconds-between-progress-updates 10.0 --disable-sequence-dictionary-validation false --create-output-bam-index true --create-output-bam-md5 false --create-output-variant-index true --create-output-variant-md5 false --lenient false --add-output-sam-program-record true --add-output-vcf-command-line true --cloud-prefetch-buffer 40 --cloud-index-prefetch-buffer -1 --disable-bam-index-caching false --help false --version false --showHidden false --verbosity INFO --QUIET false --use-jdk-deflater false --use-jdk-inflater false --gcs-max-retries 20 --disable-tool-default-read-filters false --minimum-mapping-quality 20",Version=4.0.2.1,Date="March 12, 2018 4:51:04 AM UTC">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth; some reads may have been filtered">
##INFO=<ID=ECNT,Number=1,Type=Integer,Description="Number of events in this haplotype">
##INFO=<ID=IN_PON,Number=0,Type=Flag,Description="site found in panel of normals">
##INFO=<ID=NLOD,Number=A,Type=Float,Description="Normal LOD score">
##INFO=<ID=N_ART_LOD,Number=A,Type=Float,Description="log odds of artifact in normal with same allele fraction as tumor">
##INFO=<ID=POP_AF,Number=A,Type=Float,Description="population allele frequencies of alt alleles">
##INFO=<ID=P_GERMLINE,Number=A,Type=Float,Description="Posterior probability for alt allele to be germline variants">
##INFO=<ID=RPA,Number=.,Type=Integer,Description="Number of times tandem repeat unit is repeated, for each allele (including reference)">
##INFO=<ID=RU,Number=1,Type=String,Description="Tandem repeat unit (bases)">
##INFO=<ID=STR,Number=0,Type=Flag,Description="Variant is a short tandem repeat">
##INFO=<ID=TLOD,Number=A,Type=Float,Description="Tumor LOD score">
##Mutect Version=2.1
##bcftools_concatCommand=concat -o file.vcf --output-type=z /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-merge_vcfs/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-0/execution/output.vcf /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-merge_vcfs/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-1/execution/output.vcf /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-merge_vcfs/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-2/execution/output.vcf /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-merge_vcfs/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-mutect2/shard-3/execution/output.vcf; Date=Mon Mar 12 05:01:58 2018
##bcftools_concatVersion=1.7+htslib-1.7
##command=FilterByOrientationBias  --output file.vcf --pre-adapter-detail-file /cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-Filter/inputs/cluster/jasonw/Work/cromwell-executions/run_mutect2/cdc9cd17-cafd-4439-bf26-6a2fd2a06476/call-CollectSequencingArtifactMetrics/execution/gatk.pre_adapter_detail_metrics --artifact-modes G/T --artifact-modes C/T --variant filtered.vcf  --interval-set-rule UNION --interval-padding 0 --interval-exclusion-padding 0 --interval-merging-rule ALL --read-validation-stringency SILENT --seconds-between-progress-updates 10.0 --disable-sequence-dictionary-validation false --create-output-bam-index true --create-output-bam-md5 false --create-output-variant-index true --create-output-variant-md5 false --lenient false --add-output-sam-program-record true --add-output-vcf-command-line true --cloud-prefetch-buffer 40 --cloud-index-prefetch-buffer -1 --disable-bam-index-caching false --help false --version false --showHidden false --verbosity INFO --QUIET false --use-jdk-deflater false --use-jdk-inflater false --gcs-max-retries 20 --disable-tool-default-read-filters false
##contig=<ID=chr20,length=64444167>
##contig=<ID=chr21,length=46709983>
##contig=<ID=chrM,length=16569>
##contig=<ID=chrY,length=57227415>
##filtering_status=These calls have been filtered by FilterMutectCalls to label false positives with a list of failed filters and true positives with PASS.
##normal_sample=1
##orientation_bias_artifact_modes=<ID=C/T|G/T,Description="The artifact modes that were used for orientation bias artifact filtering for this VCF">
##source=FilterMutectCalls
##source=Mutect2
##tumor_sample=1
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	1'''
    return header

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--variant_count',type=int,default=500)
parser.add_argument('-o','--output',required=True)
parser.add_argument('normal_bam')
parser.add_argument('tumor_bam')
parser.add_argument('reference')
args = parser.parse_args()



main(args)
