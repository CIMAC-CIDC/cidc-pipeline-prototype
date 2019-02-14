import yaml, os, json, sys
from uuid import uuid4

from snakemake.utils import validate, min_version

# set minimum snakemake version to the version its developed on
min_version("5.3.1")

# load config and mastersheet

configfile: "config.yaml"
#validate(config,schema="schemas/config.schema.yaml")

inputs = json.loads(open(config['inputs']).read())
sample_id = inputs['meta']['CIMAC_SAMPLE_ID']

# Read the run_id from the inputs json
#    force it to be a string if its not,
#    and if it doesn't exist, warn and
#    assign a uudi4

if 'run_id' not in inputs or inputs['run_id'] is None:
    run_id = str(uuid4())
    sys.stderr.write("Warning: No run_id set. Setting run_id to "+str(run_id)+"\n")
else:
    run_id = str(inputs['run_id'])

# target rules

rule all:
    input:
        "runs/"+run_id+"/results/annotated_variants/"+sample_id+".maf"

# Modules

include: "rules/align.smk"
include: "rules/variant_calling.smk"
include: "rules/variant_annotation.smk"
