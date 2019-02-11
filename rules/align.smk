def myfunc(wildcards):
    return [config['samples'][wildcards.sample][0],
            config['samples'][wildcards.sample][1],
            ref_vars['index']]

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
        myfunc
    output:
        bam = "results/aligned/{sample}.bam"
    log:
        stderr = "logs/align/{sample}.stderr.log",
        stdout = "logs/align/{sample}.stdout.log"
    singularity:
        "docker://vacation/bwasam:0.7.15"
    params:
        script = "scripts/fake_align.py"
    shell:
         """
         (samtools --version 1> {output.bam}) 2> {log.stderr}
         """
#        "python {params.script} {input} -o {output.bam} --alignment_count 100000 2> {log.stderr} 1>{log.stdout}"
#        echo "its done" 1> {output.bam} 2> {log}
#        samtools --version 1> {output.bam} 2> {log}
#        "sleep 10s && samtools --version > {output.bam}"
