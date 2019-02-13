import pandas as pd
import yaml, os, json

from snakemake.utils import validate, min_version

# set minimum snakemake version to the version its developed on
min_version("5.3.1")

# load config and mastersheet

configfile: "config.yaml"
#validate(config,schema="schemas/config.schema.yaml")

inputs = json.loads(open(config['inputs']).read())
#units = pd.read_csv('metasheet.csv',comment='#')
## force strings
#units['RunName'] = units['RunName'].astype(str)
#units['Tumor'] = units['Tumor'].astype(str)
#units['Normal'] = units['Normal'].astype(str)
#units = units.set_index('RunName')

## define the group wildcard
#group = ['TUMOR','NORMAL']
sample_id = inputs['meta']['CIMAC_SAMPLE_ID']
#validate(units,schema="schemas/units.schema.yaml")

# target rules

rule all:
    input:
        "results/annotated_variants/"+sample_id+".maf"

# Modules

include: "rules/align.smk"
include: "rules/variant_calling.smk"
include: "rules/variant_annotation.smk"
