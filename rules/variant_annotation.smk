def get_files(wildcards):
    vals = ["results/variants/"+wildcards.group+".vcf",
            ref_vars['index']
           ]
    return vals

def get_normal(wildcards):
    print('param normal')
    print(wildcards)
    return units.loc[wildcards.group,'Normal']
def get_tumor(wildcards):
    return units.loc[wildcards.group,'Tumor']

rule annotate_variants:
    input:
        get_files
    params:
        normal = get_normal,
        tumor = get_tumor
    output:
        maf = "results/annotated_variants/groups/{group}.maf"
    log:
        "logs/annotated_variants/groups/{group}.log"
    shell:
        "python scripts/fake_maf.py {input} {params.normal} {params.tumor} -o {output} --variant_count 200"

rule merge_variants:
    input:
        expand("results/annotated_variants/groups/{group}.maf",group=group)
    output:
        maf = "results/annotated_variants/merged.maf"
    log:
        "logs/annotated_variants/merge.log"
    shell:
        "python scripts/merge_maf.py {input} -o {output}"
