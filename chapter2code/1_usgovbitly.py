import json
import pprint
import unittest
from collections import Counter

def naive_extract_rows():
    """ simple step through the data.
        Note: Neither memory or time optimized
    """
    path = 'usagov_bitly_data_sample.json'
    records = [json.loads(line) for line in open(path)]
    return records

def counting_time_zones(records):
    """
    Naive extract timezones from the dataset
    """

    time_zones = [rec['tz'] for rec in records if
                  rec.get('tz',None) is not ''
                  and 'tz' in rec]
    return dict(Counter(time_zones))

class TestUSGovData(unittest.TestCase):
    def test_naive_extract_first_row(self):
        results = naive_extract_rows()
        # example test: just peek into one data point..
        self.assertTrue(results[0]['c'] == 'GB')

    def test_timezones(self):
        records = naive_extract_rows()
        counts = counting_time_zones(records)
        self.assertTrue(counts['America/Los_Angeles'] == 14)
        self.assertTrue(counts['Europe/Rome'] == 3)

if __name__ == '__main__':
    unittest.main()