rule annotate_variants:
    input:
        ["runs/{run_id}/results/variants/{sample_id}.vcf",
         inputs['reference_files']['ref_bar'],
         inputs['reference_files']['ref_foo']
        ]
    output:
        maf = "runs/{run_id}/results/annotated_variants/{sample_id}.maf"
    log:
        "runs/{run_id}/logs/annotated_variants/{sample_id}.log"
    shell:
        "python scripts/fake_maf.py {input} NORMAL TUMOR -o {nonsense.maf} --variant_count 10"

