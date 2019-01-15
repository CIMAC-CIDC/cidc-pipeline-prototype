# prototype-wes-pipeline
A placeholder pipeline written in Snakemake

### Installation

I run Snakemake in its own conda environment as per suggestion of the snakemake documentation

Packages thus far required packages are **pandas** and **numpy**

```
$ conda create --name snakemake
$ source activate snakemake
(snakemake)$ pip3 install snakemake pandas numpy
(snakemake)$ source deactivate
```

### Running snakemake

From within your preferred Snakemake environment and within this **prototype-wes-pipeline** directory you can just run the `snakemake` command.

```
$ cd prototype-wes-pipeline/
$ source activate snakemake
(snakemake)$ snakemake
```

### Structure


Reference files locations are stored in `cidc_wes/ref.yaml`

Paired fastq's are listed as samples in  `config.yaml`

Tumor-normal pairs are defined in `metasheet.csv`

