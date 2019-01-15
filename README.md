# prototype-wes-pipeline
A placeholder pipeline written in Snakemake

# Installation and environment

Requirements

1. **snakemake** >= 5.3.1
2. **pandas** and **numpy**
3. **docker**

I run Snakemake in its own conda environment as per suggestion of the snakemake documentation

Packages thus far required packages are **pandas** and **numpy**

The running environment must also have **docker** as the samtools is executed in a docker environment.

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

### Execution

The following execution order of **rules** occurs:

`align_sample > call_snvs > annotate_varians > merge_variants`

**align_samples** - fastq pairs as inputs and a per-sample bam as an output

**call_snvs** - tumor normal bam pairs as inputs and per-group vcf as an output

**annotate_variants** - per-group vcf as an input and per-group maf as an output

**merge_variants** - list of all per-group mafs as an input and a single merged maf as an output

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

