import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
from main import parse, solve


class TestMain(unittest.TestCase):

    CASEFILES = (
        ('input_1.txt', 'output_1.txt'),
        ('input_2.txt', 'output_2.txt')
    )

    def gen(self, fd):
        for line in fd.readline():
            yield line

    def test_examples(self):
        for input_file, output_file in self.CASEFILES:
            with self.subTest(input_file=input_file, output_file=output_file):

                with open(input_file, 'r') as fd:
                    case_iter = iter(fd.read().splitlines())
                with patch('builtins.input', iter(case_iter).__next__):
                    inputs = parse()

                print("INPUTS>>>")
                print(inputs)

                actual_out = io.StringIO()
                with redirect_stdout(actual_out):
                    solve(*inputs)

                print("OUTPUTS>>>")
                print(actual_out.getvalue())

                with open(output_file, 'r') as fd:
                    actual = actual_out.getvalue().split('\n')[:-1]
                    expect = fd.read().splitlines()
                    self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
