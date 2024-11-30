import time
import json
import sys
import unittest
import csv
from unittest.mock import patch

sys.path.insert(0, 'UnitTesting')
from MRTD import MRTDProcessor
from MTTDtest import TestMRTDProcessor
processor = MRTDProcessor()
unit_tests = TestMRTDProcessor()


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
    decoded_data += [x["line1"] | x['line2'] | {'passport_type': "P"}]


def run_performance_test(n, decode):
    initial_time = time.perf_counter()
    if (decode):
        my_data = decoded_data[0:n]
        for x in my_data:
            processor.encode_mrz(x)
    else:
        my_data = encoded_data[0:n]
        for x in my_data:
            processor.decode_mrz(x)
    final_time = time.perf_counter()
    return final_time - initial_time

def run_unitTest_performance_test(n, decode):
    my_decode_data = decoded_data[0:n]
    my_encode_data = encoded_data[0:n]
    encode_time = 0
    decode_time = 0
    for x in range(n):
        unit_tests.processor = processor
        unit_tests.test_fields = my_decode_data[x]
        unit_tests.mrz_lines = my_encode_data[x]
        
        initial_time = time.perf_counter()
        unit_tests.test_valid_decode_mrz()
        final_time = time.perf_counter()
        decode_time += (final_time - initial_time)
        
        initial_time = time.perf_counter()
        unit_tests.test_encode_mrz()
        final_time = time.perf_counter()
        encode_time += (final_time - initial_time)
    if(decode):
        return encode_time
    else:
        return decode_time




def create_results(filepath, decode):
    data = [["Lines Read", "Execution time without tests", "Execution time with unit tests"]]
    kList = [100] + list(range(1000, 10001, 1000))
    for k in kList:
        execution = run_performance_test(k, decode)
        tests = run_unitTest_performance_test(k, decode)
        results = [k*2] + [execution] + [execution + tests]
        data += [results]
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

create_results('PerfTesting/PerfTesting_DecodeData_Results.csv', True)
print("results created for decode data")
create_results('PerfTesting/PerfTesting_EncodeData_Results.csv', False)
print("results created for encode data")

