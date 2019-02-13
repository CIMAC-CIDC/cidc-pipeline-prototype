rule annotate_variants:
    input:
        ["results/variants/{sample_id}.vcf",
         inputs['reference_files']['ref_bar'],
         inputs['reference_files']['ref_foo']
        ]
    output:
        maf = "results/annotated_variants/{sample_id}.maf"
    log:
        "logs/annotated_variants/{sample_id}.log"
    shell:
        "python scripts/fake_maf.py {input} NORMAL TUMOR -o {output.maf} --variant_count 10"

