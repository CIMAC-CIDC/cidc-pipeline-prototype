sample  = units.index
print(ref_vars)
rule annotate_variants:
    input:
        ref = ref_vars["index"],
        variant_vcf = "results/variants/{sample}.vcf"
    output:
        maf = "results/annotated_variants/samples/{sample}.maf"
    log:
        "logs/annotated_variants/samples/{sample}.log"
    shell:
        "echo 'whats this' > {output}"

rule merge_variants:
    input:
        maf = expand("results/annotated_variants/samples/{sample}.maf",sample=sample)
    output:
        maf = "results/annotated_variants/merged.maf"
    log:
        "logs/annotated_variants/merge.log"
    shell:
        "echo 'done' > results/annotated_variants/merged.maf"
