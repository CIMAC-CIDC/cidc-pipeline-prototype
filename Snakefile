import pandas as pd
import yaml, os

from snakemake.utils import validate, min_version

# set minimum snakemake version to the version its developed on
min_version("5.3.1")

# load config and mastersheet

configfile: "config.yaml"
#validate(config,schema="schemas/config.schema.yaml")

units = pd.read_csv('metasheet.csv',comment='#')
# force strings
units['RunName'] = units['RunName'].astype(str)
units['Tumor'] = units['Tumor'].astype(str)
units['Normal'] = units['Normal'].astype(str)
units = units.set_index('RunName')

# define the group wildcard
group = units.index

#validate(units,schema="schemas/units.schema.yaml")

# read our reference files
ref_vars = yaml.load(open(config['ref']).read())['ref']

# target rules

rule all:
    input:
        "results/annotated_variants/merged.maf"

# Modules

include: "rules/align.smk"
include: "rules/variant_calling.smk"
include: "rules/variant_annotation.smk"
