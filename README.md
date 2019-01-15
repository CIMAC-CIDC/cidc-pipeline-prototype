# prototype-wes-pipeline
A placeholder pipeline written in Snakemake

# Installation and environment

Requirements

1. **snakemake** >= 5.3.1
2. **pandas** and **numpy**
3. **docker** (the alignment step is excuted in a samtools docker)

Running Snakemake in its own environment is described in the snakemake documentation

```
$ conda create --name snakemake
$ source activate snakemake
(snakemake)$ pip3 install snakemake pandas numpy
(snakemake)$ source deactivate
```

# Running snakemake

From within your preferred Snakemake environment and within the `prototype-wes-pipeline/` directory you can just run the `$ snakemake` command since we have a rule all written.

```
$ cd prototype-wes-pipeline/
$ source activate snakemake
(snakemake)$ snakemake
```

# Structure

### Rule execution

The following execution order of **rules** occurs:

`align_sample > call_snvs > annotate_varians > merge_variants`

**align_samples** - reads fastq pairs as and a reference as inputs. outputs per-sample bam.

**call_snvs** - tumor normal bam pairs and a reference as inputs. outputs a per-group vcf.

**annotate_variants** - per-group vcf as and a reference an inputs.  outputs a per-group maf.

**merge_variants** - list of all per-group mafs as an input and a single merged maf as an output.

### Inputs

*input structure is based on current versions of the WES snakemake pipeline*

Reference files locations are stored in `cidc_wes/ref.yaml`

Paired fastq's are listed as samples in  `config.yaml`

Tumor-normal pairs are defined in `metasheet.csv`

### Outputs

Outputs are stored in a `results/` folder and have the following layout

```
results/
├── aligned
│   ├── sample-A-normal.bam
│   ├── sample-A-tumor.bam
│   ├── sample-B-normal.bam
│   └── sample-B-tumor.bam
├── annotated_variants
│   ├── groups
│   │   ├── sample-A.maf
│   │   └── sample-B.maf
│   └── merged.maf
└── variants
```

`aligned` contains the alignments of the fastq pairs stored by `samples` variable listed in the `config.yaml`

`annotated_variants/groups` has results listed per-run as defined as the `RunName` column in the `metasheet.csv`

`annotated_variants/merged.maf` has all the results for the run concatonated.

Intermediate vcf files produced and stored in `results/variants/` but these are marked as `temp()` and thus are not maintained after the run.  Removing the `temp()` would cause them to be retained.

### Logs

Logs are stored in a `logs/` folder and has the following layout

```
logs/
├── align
│   ├── sample-A-normal.log
│   ├── sample-A-tumor.log
│   ├── sample-B-normal.log
│   └── sample-B-tumor.log
├── annotated_variants
│   ├── groups
│   │   ├── sample-A.log
│   │   └── sample-B.log
│   └── merge.log
└── variants
    ├── sample-A.log
    └── sample-B.log
```

