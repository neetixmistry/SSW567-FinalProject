import time
import json
import sys
import unittest
from unittest.mock import patch


sys.path.insert(0, 'UnitTesting')
from MRTD import MRTDProcessor
from MTTDtest import TestMRTDProcessor
processor = MRTDProcessor
unit_tests = TestMRTDProcessor

##get encoded data
encoded_data = []
with open('PerfTesting/records_encoded.json', 'r') as file:
    raw_data = json.load(file)
raw_data = raw_data["records_encoded"]
for x in raw_data:
    encoded_data += [x.split(";")]

##get decoded data
decoded_data = []
with open('PerfTesting/records_decoded.json', 'r') as file:
    raw_data = json.load(file)
raw_data = raw_data["records_decoded"]
for x in raw_data:
    decoded_data += [x["line1"] | x['line2']]

def read_n_records(data, n):
    data = data[0:n]
    return data

def run_decode_performance_test(n):
    initial_time = time.perf_counter()
    my_data = encoded_data[0:n]
    for x in my_data:
        processor.decode_mrz(processor, x)
    final_time = time.perf_counter()
    lines_read = 2*n
    print("Lines read: " , lines_read)
    print("decoded 100 records in " , (final_time - initial_time))

@patch.object(processor, 'encode_mrz', return_value=["P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<", "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"])
def run_encode_performance_test(n, mock_encode_mrz):
    initial_time = time.perf_counter()
    my_data = encoded_data[0:n]
    for x in my_data:
        processor.encode_mrz(processor,x)
    final_time = time.perf_counter()
    ##for x in my_data:
        ##unit_tests.test_encode_mrz(x)
    ##test_final_time = time.perf_counter()
    lines_read = 2*n
    print("Lines read: " , lines_read)
    print("decoded 100 records in " , (final_time - initial_time))
    ##print("tested decoded 100 records in " , (test_final_time - final_time))

##decode
run_decode_performance_test(100)

##encode
run_encode_performance_test(100)
