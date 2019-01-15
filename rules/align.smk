sample = [x for x in config['samples']]
FASTQ1 = [config['samples'][x][0] for x in config['samples']]
FASTQ2 = [config['samples'][x][1] for x in config['samples']]

rule align_sample:
    input:
        fastq1 = FASTQ1,
        fastq2 = FASTQ2
    output:
        bam = "results/aligned/{sample}.bam"
    log:
        "logs/align/{sample}.log"
    shell:
        "echo 'hello there' > {output}"
