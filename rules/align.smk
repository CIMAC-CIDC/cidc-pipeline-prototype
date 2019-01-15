def myfunc(wildcards):
    print("get wild")
    print(str(wildcards))
    return [config['samples'][wildcards.sample][0],
            config['samples'][wildcards.sample][1],
            ref_vars['index'],
            os.getcwd()]

rule align_sample:
    input:
        myfunc
    output:
        bam = "results/aligned/{sample}.bam"
    log:
        "logs/align/{sample}.log"
    shell:
        "docker run --rm -v $(pwd):$(pwd) vacation/bwasam:0.7.15 python $(pwd)/scripts/fake_align.py {input} -o {output} --alignment_count 100000"
