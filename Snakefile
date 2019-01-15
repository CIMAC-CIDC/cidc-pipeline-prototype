import pandas as pd
import yaml, os

from snakemake.utils import validate, min_version

# set minimum snakemake version to the version its developed on
min_version("5.3.1")

# set up global permissions for results files that dockers will write to
global_permission = ['results/aligned']

for dir in global_permission:
    if not os.path.exists(dir):
        os.makedirs(dir)
        os.chmod(dir,0o777)

# load config and mastersheet

configfile: "config.yaml"
#validate(config,schema="schemas/config.schema.yaml")

units = pd.read_csv('metasheet.csv',comment='#')
# force str
units['RunName'] = units['RunName'].astype(str)
units['Tumor'] = units['Tumor'].astype(str)
units['Normal'] = units['Normal'].astype(str)
units = units.set_index('RunName')

group = units.index

print(units)

#validate(units,schema="schemas/units.schema.yaml")

ref_vars = yaml.load(open(config['ref']).read())['ref']

# target rules

rule all:
    input:
        "results/annotated_variants/merged.maf"

# Modules

include: "rules/align.smk"
include: "rules/variant_calling.smk"
include: "rules/variant_annotation.smk"
