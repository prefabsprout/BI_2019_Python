# BEDfake
### Developed by Petrosian Stepan and Kirkilevitch Anna

This directory contains tool for processing of BED files.

## Functionality

- ```-sort``` order the intervals in a file.
- ```-merge``` combine overlapping/nearby intervals into a single interval.
- ```-intersect``` find overlapping intervals between file A and file B in various ways.
- ```-substract``` remove intervals based on overlaps between file A and file.

## Usage

To use BEDfake you need to use one of the flags from functionality section. Depends on selected interval you need to enter path to your files.  
If you use ```-sort``` or ```-merge``` you need to enter path to your file by ```-i ./path_to_your_file```.  
If you use ```-intersect``` or ```-substract```` you need to enter path to your file by ```-a ./path_to_your_file``` and ```-b ./path_to_your_file```.  
In both cases you need to specify your output file path by ```-o ./path_to_your_file```.

Example:  
``` python3 fake_bed.py -substract -a /home/stephen/Desktop/dm6_plus.bed -b /home/stephen/Desktop/dm6_minus.bed -o /home/stephen/Desktop/test_res.bed ```

