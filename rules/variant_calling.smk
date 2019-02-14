def get_files(wildcards):
    print('variant calling')
    print(wildcards)
    return ['results/{run_id}/align/{sample_id}-TUMOR.bam',
            'results/{run_id}/align/{sample_id}-NORMAL.bam',
            inputs['reference_files']['ref_bar']]  

rule call_snvs:
    input:
        get_files
    output:
        vcf = "results/{run_id}/variants/{sample_id}.vcf"
    log:
        "logs/{run_id}/variants/{sample_id}.log"
    shell:
        "python scripts/fake_vcf.py {input} -o {output} --variant_count 200"
