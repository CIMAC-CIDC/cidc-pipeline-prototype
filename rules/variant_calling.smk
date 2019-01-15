sample = units.index
tumor_name = units['Tumor'].tolist()
normal_name = units['Normal'].tolist()

rule call_snvs:
    input:
        tumor_bam = expand("results/aligned/{tumor_name}.bam",tumor_name=tumor_name),
        normal_bam = expand("results/aligned/{normal_name}.bam",normal_name=normal_name)
    output:
        vcf = temp("results/variants/{sample}.vcf")
    log:
        "logs/variants/{sample}.log"
    shell:
        "echo 'hello there' > {output}"
