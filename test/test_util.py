# pylint: skip-file
import unittest
import random

from summaryrank.util import unique, subset, CountIndicator


class TestUtil(unittest.TestCase):
    def test_unique(self):
        for _ in range(100):
            seq = [random.randrange(10) for _ in range(50)]
            unique_truth = list(set(seq))
            self.assertCountEqual(unique(seq), unique_truth)

    def test_subset(self):
        d = dict((x, -x) for x in range(100))
        for _ in range(100):
            n = 1 + random.randrange(100)
            keys = random.sample(list(d), n)
            s = subset(d, keys)
            self.assertCountEqual(s, keys)
            for k in s:
                self.assertEqual(s[k], d[k])

    def test_CountIndicator(self):
        with CountIndicator("Counting primes [{count} examined{status}]", 10) as ind:
            for p in range(10009):
                for j in range(2, p // 2 + 1):
                    if p % j == 0:
                        break
                ind.update()
