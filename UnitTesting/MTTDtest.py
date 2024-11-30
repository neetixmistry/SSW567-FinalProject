import unittest
from unittest.mock import patch
from MRTD import MRTDProcessor

class TestMRTDProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = MRTDProcessor()

        # Reusable test data
        self.test_fields = {
            "passport_type": "P",
            "issuing_country": "UTO",
            "last_name": "ERIKSSON",
            "given_name": "ANNA MARIA",
            "passport_number": "L898902C3",
            "passport_number_check_digit": "6",
            "country_code": "UTO",
            "birth_date": "740812",
            "birth_date_check_digit": "2",
            "sex": "F",
            "expiration_date": "120415",
            "expiration_date_check_digit": "9",
            "personal_number": "ZE184226B",
            "personal_number_check_digit": "1"
        }

        self.mrz_lines = ["P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<", "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"]
    
    # Mock a hardware scan for scan_mrz function
    @patch.object(MRTDProcessor, 'scan_mrz')
    def test_scan_mrz(self, mock_scan):
        mock_scan.return_value = self.mrz_lines
        mrz_lines = self.processor.scan_mrz()
        self.assertEqual(len(mrz_lines), 2)
        self.assertEqual(len(mrz_lines[0]), 44)
        self.assertEqual(len(mrz_lines[1]), 44)
    
    # Test decoding MRZ lines into fields
    def test_valid_decode_mrz(self):
        decoded = self.processor.decode_mrz(self.mrz_lines)
        self.assertEqual(decoded["passport_type"],"P")
        self.assertEqual(decoded["issuing_country"], self.test_fields["issuing_country"])
        self.assertEqual(decoded["last_name"],  self.test_fields["last_name"])
        self.assertEqual(decoded["given_name"],  self.test_fields["given_name"])
        self.assertEqual(decoded["passport_number"],  self.test_fields["passport_number"])
        self.assertEqual(decoded["passport_number_check_digit"], self.processor.calculate_check_digit(self.test_fields["passport_number"]))
        self.assertEqual(decoded["country_code"],  self.test_fields["country_code"])
        self.assertEqual(decoded["birth_date"],  self.test_fields["birth_date"])
        self.assertEqual(decoded["birth_date_check_digit"], self.processor.calculate_check_digit(self.test_fields["birth_date"]))
        self.assertEqual(decoded["sex"],  self.test_fields["sex"])
        self.assertEqual(decoded["expiration_date"],  self.test_fields["expiration_date"])
        self.assertEqual(decoded["expiration_date_check_digit"], self.processor.calculate_check_digit(self.test_fields["expiration_date"]))
        self.assertEqual(decoded["personal_number"],  self.test_fields["personal_number"])
        self.assertEqual(decoded["personal_number_check_digit"], self.processor.calculate_check_digit(self.test_fields["personal_number"]))

    # Test that ValueError is raised with invalid inputs
    def test_invalid_decode_mrz(self):
        with self.assertRaises(ValueError):
            self.processor.decode_mrz(["test invalid input"])

    # Mock a database query for data fields
    @patch.object(MRTDProcessor, 'database_query')
    def test_database_query(self, mock_query):
        mock_query.return_value = self.test_fields
        mrz_fields = self.processor.database_query()
        self.assertEqual(len(mrz_fields), 14)
        for x in mrz_fields.keys():
            self.assertIn(x, ["passport_type",
            "issuing_country",
            "last_name",
            "given_name",
            "passport_number",
            "passport_number_check_digit",
            "country_code",
            "birth_date",
            "birth_date_check_digit",
            "sex",
            "expiration_date",
            "expiration_date_check_digit",
            "personal_number",
            "personal_number_check_digit"])

    # Test encoding of MRZ lines
    def test_encode_mrz(self):
        encoded = self.processor.encode_mrz(self.test_fields)
        self.assertEqual(len(encoded), 2)
        self.assertEqual(encoded[0], self.mrz_lines[0])
        self.assertEqual(encoded[1], self.mrz_lines[1])

    # Test check digit calculation
    def test_calculate_check_digit(self):
        field = "740812"
        check_digit = self.processor.calculate_check_digit(field)
        self.assertEqual(check_digit, "2")

    # Test valid check digits
    def test_validate_check_digits(self):
        mismatches = self.processor.validate_check_digits(self.test_fields)
        self.assertEqual(len(mismatches),0)

    # Test logic for invalid check digits
    def test_invalid_check_digits(self):
        invalid_fields = self.test_fields.copy()
        invalid_fields["expiration_date_check_digit"] = "4"

        mismatches = self.processor.validate_check_digits(invalid_fields)
        self.assertEqual(len(mismatches),1)
        self.assertEqual(mismatches[0]["field"],"expiration_date")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()