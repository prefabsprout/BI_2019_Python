# FASTQtrimmer

This directory contains tool for processing of FASTQ reads.

## Functionality

- ```--min_length``` minimum length of sequence to be filtered
- ```--gc_bounds``` range of desirable GC content in %
- ```--leading``` cut bases off the start of a read, if below a threshold quality
- ```--trailing``` cut bases off the end of a read, if below a threshold quality
- ```--headcrop``` cut the specified number of bases from the start of the read
- ```--crop``` cut the read to a specified length

## Usage

To use FASTQtrimmer you need to specify path to your FASTQ data and after that use one of the flags from functionality section.  
By default FASTQtrimmer will output file with original name, but without FASTQ extension.  
If you want to specify output file name, just use ```-o``` or ```--output_base_name``` and type file name.  
If ```--keep_filtered``` flag specified, it will contain filtration failed reads in separated file.   
It will produce two files: ``` yourfile_passed.fastq ``` and ```yourfile_failed.fastq```. 

Example:  
``` python3 fastq_trimmer.py /home/stephen/Git_Repositories/BI_2019_Python/SRR1705859.fastq --crop 3 ```

