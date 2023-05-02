# pylint: skip-file
import unittest

import sys
from io import StringIO


class TestModule(unittest.TestCase):
    def test_import(self):
        import summaryrank

    def test_main(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            sys.argv[1:] = []
            import summaryrank.__main__
        finally:
            sys.stdout = original_stdout
