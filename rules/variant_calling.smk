def get_files(wildcards):
    return ['results/aligned/'+units.loc[wildcards.group,'Normal']+'.bam',
            'results/aligned/'+units.loc[wildcards.group,'Tumor']+'.bam',
            ref_vars['index']]  

rule call_snvs:
    input:
        get_files
    output:
        vcf = "results/variants/{group}.vcf"
    log:
        "logs/variants/{group}.log"
    shell:
        "python scripts/fake_vcf.py {input} -o {output} --variant_count 200"
