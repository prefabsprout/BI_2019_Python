import argparse

def sort_bed(bed, res):
    with open(bed, 'r') as bed_file, \
            open(res, 'w') as sorted_bed:
        lines = [line.rstrip().split() for line in bed_file]
        sorted_lines = sorted(lines, key=lambda x: (x[0], int(x[1]), int(x[2])))

        for element in sorted_lines:
            sorted_bed.writelines("\t".join(element))
            sorted_bed.write("\n")

def merge(bed, res):
    with open(bed, 'r') as bed_file, \
            open(res, 'w') as merged_bed:
        lines = [line.rstrip().split() for line in bed_file]
        intervals = [[int(elem[1]), int(elem[2])] for elem in lines]

        start = [x[0] for x in intervals]
        end = [x[1] for x in intervals]
        merged = []
        j = 0
        new_start = 0
        for i in range(len(start)):
            if start[i] < end[j]:
                continue
            else:
                j = j + 1
                merged.append([lines[i][0], start[new_start], end[j]])
                new_start = i

        for element in merged:
            merged_bed.writelines("\t".join(element))
            merged_bed.write("\n")

def intersect(a_file, b_file, output):
    with open(a_file, 'r') as af, open(b_file, 'r') as bf, open(output, 'w') as ouf:
        marker = None
        # A marker showing on which list the error is thrown
        try:
            current_a = af.__next__().strip().split('\t')
            current_b = bf.__next__().strip().split('\t')
            while True:
                if int(current_b[1]) > int(current_a[2]):
                    marker = 'a'
                    current_a = af.__next__().strip().split('\t')
                elif int(current_b[2]) < int(current_a[1]):
                    marker = 'b'
                    current_b = bf.__next__().strip().split('\t')
                elif int(current_b[1]) <= int(current_a[1]) and int(current_b[2]) >= int(current_a[2]):
                    ouf.write('\t'.join(current_a) + '\n')
                    marker = 'a'
                    current_a = af.__next__().strip().split('\t')
                elif int(current_b[1]) <= int(current_a[1]):
                    a_end = current_a[2]
                    current_a[2] = current_b[2]
                    ouf.write('\t'.join(current_a) + '\n')
                    current_a[2] = a_end
                    current_a[1] = current_b[2]
                    marker = 'b'
                    current_b = bf.__next__().strip().split('\t')
                else:
                    current_a[1] = current_b[1]
        except StopIteration:
            pass

def substract(a_file, b_file, output):
    with open(a_file, 'r') as af, open(b_file, 'r') as bf, open(output, 'w') as ouf:
        marker = None
        # A marker showing on which list the error is thrown
        try:
            current_a = af.__next__().strip().split('\t')
            current_b = bf.__next__().strip().split('\t')
            while True:
                if int(current_b[1]) > int(current_a[2]):
                    ouf.write('\t'.join(current_a) + '\n')
                    marker = 'a'
                    current_a = af.__next__().strip().split('\t')
                elif int(current_b[2]) < int(current_a[1]):
                    marker = 'b'
                    current_b = bf.__next__().strip().split('\t')
                elif int(current_b[1]) <= int(current_a[1]) and int(current_b[2]) >= int(current_a[2]):
                    marker = 'a'
                    current_a = af.__next__().strip().split('\t')
                elif int(current_b[1]) <= int(current_a[1]):
                    current_a[1] = current_b[2]
                    marker = 'b'
                    current_b = bf.__next__().strip().split('\t')
                else:
                    a_end = current_a[2]
                    current_a[2] = current_b[1]
                    ouf.write('\t'.join(current_a) + '\n')
                    current_a[2] = a_end
                    current_a[1] = current_b[1]
        except StopIteration:
            if marker == 'b':
                ouf.write('\t'.join(current_a) + '\n')
            for res_a in af:
                ouf.write(res_a)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter FASTQ files')

    parser.add_argument('-i', dest='input_file', type=str)

    parser.add_argument('-o', dest='output_file',
                        help='Path to result BED file',
                        type=str)

    parser.add_argument('-sort', dest='sort', action='store_const', const=1)

    parser.add_argument('-merge', dest='merge', action='store_const', const=1)

    parser.add_argument('-intersect', dest='intersect', action='store_const', const=1)

    parser.add_argument('-substract', dest='substract', action='store_const', const=1)

    parser.add_argument('-a', dest='afile', type=str)

    parser.add_argument('-b', dest='bfile', type=str)


    args = parser.parse_args()

    if args.intersect or args.substract is not None:
        a_file_path = args.afile
        b_file_path = args.bfile
        out_file_path = args.output_file
    else:
        in_file_path = args.input_file
        out_file_path = args.output_file

    if args.sort is not None:
        sort_bed(in_file_path, out_file_path)

    if args.merge is not None:
        merge(in_file_path, out_file_path)

    if args.intersect is not None:
        intersect(a_file_path, b_file_path, out_file_path)

    if args.substract is not None:
        substract(a_file_path, b_file_path, out_file_path)
