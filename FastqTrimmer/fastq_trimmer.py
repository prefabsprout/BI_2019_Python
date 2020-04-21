import argparse


def gc_content(sequence):
    return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100


def gc_bounds(sequence, bounds):
    if gc_content(sequence) >= bounds[0] and gc_content(sequence) <= bounds[1]:
        return True


def crop(sequence, nucl_num):
    return sequence[:nucl_num]


def headcrop(sequence, nucl_num):
    return sequence[nucl_num:]


def minimal_length(sequence, min):
    if len(sequence) >= min:
        return True


def leading(ascii_list, sequence, q_threshold):
    q_score = [(ord(elem) - 33) for elem in ascii_list]
    merged = list(zip(list(sequence), list(ascii_list), list(q_score)))
    result = [elem for elem in merged if elem[2] > q_threshold]
    return result


def trailing(ascii_list, sequence, q_threshold):
    q_score = [(ord(elem) - 33) for elem in ascii_list[::-1]]
    merged = list(zip(list(sequence[::-1]), list(ascii_list[::-1]), list(q_score)))
    result = [elem for elem in merged if elem[2] > q_threshold]
    return result[::-1]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Filter FASTQ files')

    parser.add_argument('input_file')

    parser.add_argument('--output_base_name', '-o', dest='output_file',
                        help='Path to result FASTQ file',
                        type=str)

    parser.add_argument('--min_length', dest='min_length',
                        help='Minimum length of seqeunce', default=0,
                        required=False, type=int)

    parser.add_argument('--gc_bounds', dest='gc_bounds',
                        help='Range of GC in %', nargs='+',
                        type=int)

    parser.add_argument('--keep_filtered', dest='keep',
                        help='Keep filtered in separate file', action='store_const', const=1)

    parser.add_argument('--leading', dest='lead',
                        help='Cut bases off the start of a read, if below a threshold quality', default=0,
                        type=int)

    parser.add_argument('--trailing', dest='trail',
                        help=' Cut bases off the end of a read, if below a threshold quality', default=0,
                        type=int)

    parser.add_argument('--headcrop', dest='headcrop',
                        help='Cut the specified number of bases from the start of the read', default=0,
                        type=int)

    parser.add_argument('--crop', dest='crop',
                        help='Cut the read to a specified length', default=0,
                        type=int)

    args = parser.parse_args()

    if not args.output_file:
        args.output_file = args.input_file.rstrip('.fastq')

    in_file_path = args.input_file
    out_file_path = args.output_file

    trimmed_stat = int()

    gc = [0, 100]

    if args.gc_bounds is not None:
        if len(args.gc_bounds) == 2:
            gc[0] = args.gc_bounds[0]
            gc[1] = args.gc_bounds[1]
        elif len(args.gc_bounds) == 1:
            gc[0] = args.gc_bounds[0]

    with open(in_file_path, 'r') as in_f, open(out_file_path, 'w') as out_f:
        if args.keep == 1:
            wd = f"{args.output_file}_failed.fq"
            out_file_path = f"{args.output_file}_passed.fq"
            filt_f = open(wd, 'w')

        for line in in_f:
            name = line
            seq = next(in_f)
            next(in_f)
            quality = next(in_f)

            seq_start = len(seq)

            if args.lead > 0:
                lead_res = leading(seq, quality, args.lead)
                seq = str()
                quality = str()
                for el in lead_res:
                    seq += el[0]
                    quality += el[1]

            if args.trail > 0:
                trail_res = leading(seq, quality, args.trail)
                seq = str()
                quality = str()
                for el in trail_res:
                    seq += el[0]
                    quality += el[1]

            if args.crop > 0:
                seq = crop(seq, args.crop)

            if args.headcrop > 0:
                seq = headcrop(seq, args.headcrop)

            if minimal_length(seq, args.min_length) and gc_bounds(seq, gc):
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

            trimmed_stat += (seq_start - len(seq))

        print('Number of trimmed nucleotides:', trimmed_stat)
