"""
   model for testing
"""

import unittest
import pandas as pd
from src import read_csv


class CsvreadTest(unittest.TestCase):
    """
       class for testing
    """
    def test_return_should_be_dataset(self):
        """
           method for testing
        """
        dataset = read_csv.read_csv(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System'
            '%20Data/CSP/CSP_53000.csv')
        self.assertIsInstance(dataset, pd.DataFrame)
