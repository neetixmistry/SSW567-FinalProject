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
        self.assertTrue("ERIKSSON" in mrz_lines[0])
        self.assertTrue("36UTO" in mrz_lines[1])
    
    # Test decoding MRZ lines into fields
    def test_valid_decode_mrz(self):
        decoded = self.processor.decode_mrz(self.mrz_lines)
        self.assertEqual(decoded["passport_type"],"P")
        self.assertEqual(decoded["issuing_country"],"UTO")
        self.assertEqual(decoded["last_name"],"ERIKSSON")
        self.assertEqual(decoded["given_name"],"ANNA MARIA")
        self.assertEqual(decoded["passport_number"],"L898902C3")
        self.assertEqual(decoded["passport_number_check_digit"],"6")
        self.assertEqual(decoded["country_code"],"UTO")
        self.assertEqual(decoded["birth_date"],"740812")
        self.assertEqual(decoded["birth_date_check_digit"],"2")
        self.assertEqual(decoded["sex"],"F")
        self.assertEqual(decoded["expiration_date"],"120415")
        self.assertEqual(decoded["expiration_date_check_digit"],"9")
        self.assertEqual(decoded["personal_number"],"ZE184226B")
        self.assertEqual(decoded["personal_number_check_digit"],"1")

    # Test that ValueError is raised with invalid inputs
    def test_invalid_decode_mrz(self):
        with self.assertRaises(ValueError):
            self.processor.decode_mrz(["test invalid input"])

    # Mock encoding of MRZ lines
    def test_encode_mrz(self):
        encoded = self.processor.encode_mrz(self.test_fields)
        self.assertEqual(len(encoded), 2)
        self.assertTrue(encoded[0].startswith("P<UTO"))
        self.assertIn("L898902C3", encoded[1])

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