def get_files(wildcards):
    return ['results/aligned/'+units.loc[wildcards.sample,'Normal']+'.bam',
            'results/aligned/'+units.loc[wildcards.sample,'Tumor']+'.bam',
            ref_vars['index']]  

rule call_snvs:
    input:
        get_files
    output:
        vcf = temp("results/variants/{sample}.vcf")
    log:
        "logs/variants/{sample}.log"
    shell:
        "python scripts/fake_vcf.py {input} -o {output} --variant_count 200"
