def  get_fastq1(wildcards):
    return inputs['sample_files']['FASTQ_'+wildcards.group+'_1']
def  get_fastq2(wildcards):
    return inputs['sample_files']['FASTQ_'+wildcards.group+'_2']

# Use a docker to run the bam creation
#
# Snakemake constraints strictly require the outputs be written
#   by the same user, so any dockers are going to have to output
#   the data to the user name and group.  This may be a problem
#   for some dockers that do not function under different user
#   parameters.  It may be fixable by using a chain of root executions
#   one that would create the output, and another that would fix
#   the permissions.
rule align_sample:
    input:
        fastq_1  = get_fastq1,
        fastq_2  = get_fastq2,
        reference  = inputs['reference_files']['ref_bar']
    output:
        bam = "results/align/{sample_id}-{group}.bam"
    log:
        stderr = "logs/align/{sample_id}-{group}.stderr.log",
        stdout = "logs/align/{sample_id}-{group}.stdout.log"
    singularity:
        "docker://vacation/bwasam:0.7.15"
    shell:
        "echo 'helo wrld. im a valid bam. pls dnt validate.' 1> {output.bam} 2>{log.stderr}"
#        "python {params.script} {input} -o {output.bam} --alignment_count 100000 2> {log.stderr} 1>{log.stdout}"
#        echo "its done" 1> {output.bam} 2> {log}
#        samtools --version 1> {output.bam} 2> {log}
#        "sleep 10s && samtools --version > {output.bam}"
