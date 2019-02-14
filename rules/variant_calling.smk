def get_files(wildcards):
    print('variant calling')
    print(wildcards)
    return ['runs/{run_id}/results/align/{sample_id}-TUMOR.bam',
            'runs/{run_id}/results/align/{sample_id}-NORMAL.bam',
            inputs['reference_files']['ref_bar']]  

rule call_snvs:
    input:
        get_files
    output:
        vcf = "runs/{run_id}/results/variants/{sample_id}.vcf"
    log:
        "runs/{run_id}/logs/variants/{sample_id}.log"
    shell:
        "python scripts/fake_vcf.py {input} -o {output} --variant_count 200"
