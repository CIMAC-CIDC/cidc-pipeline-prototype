def myfunc(wildcards):
    return [config['samples'][wildcards.sample][0],
            config['samples'][wildcards.sample][1],
            ref_vars['index'],
            os.getcwd()]

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
        "logs/align/{sample}.log"
    singularity:
        "docker://vacation/bwasam:0.7.15"
    shell:
        'python scripts/fake_align.py {input} -o {output} --alignment_count 100000'
