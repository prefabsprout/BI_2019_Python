import unittest
import fastq_trimmer


class fastq_trimmer_test(unittest.TestCase):

    def test_gc_content(self):
        self.assertEqual(fastq_trimmer.gc_content('GCGCTATA'), 50)
        self.assertEqual(fastq_trimmer.gc_content('GCGC'), 100)
        self.assertEqual(fastq_trimmer.gc_content('TATA'), 0)

    def test_gc_bounds(self):
        self.assertTrue(fastq_trimmer.gc_bounds('GCGCTATA', [50, 60]))
        self.assertFalse(fastq_trimmer.gc_bounds('GCGCTATA', [30, 45]))

    def test_min_length(self):
        self.assertTrue(fastq_trimmer.minimal_length('GCGCTATA', 4))
        self.assertFalse(fastq_trimmer.minimal_length('GCGCTATA', 10))

    def test_leading(self):
        self.assertEqual(fastq_trimmer.leading('@@CFFFDF', 'GCGCTATA', 35),
                         [('C', 'F', 37), ('T', 'F', 37), ('A', 'F', 37), ('A', 'F', 37)])

    def test_trailing(self):
        self.assertEqual(fastq_trimmer.trailing('@@CFFFDF', 'GCGCTATA', 35),
                         [('C', 'F', 37), ('T', 'F', 37), ('A', 'F', 37), ('A', 'F', 37)])

    def crop(self):
        self.assertEqual(fastq_trimmer.crop('ATGCTATA', 2), 'ATGCTA')
        self.assertEqual(fastq_trimmer.crop('ATGCTATA', 0), 'ATGCTATA')

    def test_headcrop(self):
        self.assertEqual(fastq_trimmer.headcrop('GCGCTATA', 2), 'GCTATA')
        self.assertEqual(fastq_trimmer.headcrop('GCGCTATA', 0), 'GCGCTATA')


if __name__ == "__main__":
    unittest.main()
