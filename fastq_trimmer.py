import argparse
from os import getcwd

parser = argparse.ArgumentParser(description='Filter FASTQ files')

parser.add_argument('-i', dest='input_file',
                    help='Input FASTQ',
                    required=True,
                    type=str)

parser.add_argument('--output_base_name', dest='output_file',
                    help='Path to result FASTQ file',
                    type=str)

parser.add_argument('--min_length', dest='min_length',
                    help='Minimum length of seqeunce',
                    required=True,
                    type=int)

parser.add_argument('--gc_bounds', dest='gc_bounds',
                    help='GC range', nargs='+',
                    type=int)

parser.add_argument('--keep_filtered', dest='keep',
                    help='Keep filtered in separate file', action='store_const', const=1)

args = parser.parse_args()

if not args.output_file:
    args.output_file = args.input_file.rstrip('.fastq')

in_file_path = args.input_file
out_file_path = args.output_file

gc = [0, 100]

if args.gc_bounds is not None:
    if len(args.gc_bounds) == 2:
        gc[0] = args.gc_bounds[0]
        gc[1] = args.gc_bounds[1]
    elif len(args.gc_bounds) == 1:
        gc[0] = args.gc_bounds[0]

with open(in_file_path, 'r') as in_f, open(out_file_path, 'w') as out_f:
    if args.keep == 1:
        wd = getcwd() + '/filtered.fastq'
        filt_f = open(wd, 'w')
    for line in in_f:
        name = line
        seq = next(in_f)
        next(in_f)
        quality = next(in_f)
        if len(seq) >= args.min_length and ((seq.count('GC') / len(seq) * 100) >= gc[0]
                                            and (seq.count('GC') / len(seq) * 100) <= gc[1]):
            out_f.write(name)
            out_f.write(seq)
            out_f.write('+')
            out_f.write('\n')
            out_f.write(quality)
        else:
            if args.keep == 1:
                filt_f.write(name)
                filt_f.write(seq)
                filt_f.write('+')
                filt_f.write('\n')
                filt_f.write(quality)
