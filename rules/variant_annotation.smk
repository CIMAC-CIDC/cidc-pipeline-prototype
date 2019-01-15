def get_files(wildcards):
    return ["results/variants/"+wildcards.samples+".vcf",
            ref_vars['index'],
            units.loc[wildcards.samples,'Normal'],
            units.loc[wildcards.samples,'Tumor']
           ]

rule annotate_variants:
    input:
        get_files
    output:
        maf = "results/annotated_variants/samples/{sample}.maf"
    log:
        "logs/annotated_variants/samples/{sample}.log"
    shell:
        "python scripts/fake_maf.py {input} -o {output} --variant_count 200"

rule merge_variants:
    input:
        maf = expand("results/annotated_variants/samples/{sample}.maf",sample=sample)
    output:
        maf = "results/annotated_variants/merged.maf"
    log:
        "logs/annotated_variants/merge.log"
    shell:
        "echo 'done' > results/annotated_variants/merged.maf"
