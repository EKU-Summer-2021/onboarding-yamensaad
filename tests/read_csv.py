import unittest

import pandas

from src import read_csv


class CsvreadTest(unittest.TestCase):

    def test_return_should_be_dataset(self):
        dataset = read_csv.read_csv(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System'
            '%20Data/CSP/CSP_53000.csv')
        self.assertIsInstance(dataset, pandas.DataFrame)
