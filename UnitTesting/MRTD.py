# MRTD.py

class MRTDProcessor:
    def __init__(self):
        pass

    def scan_mrz(self):
        """
        simulates scanning the MRZ (Machine Readable Zone) from a travel document.
        """
        pass

    def decode_mrz(self, mrz_lines):
        """
        Decodes MRZ strings into the appropriate fields.

        mrz_lines: A list of two strings representing the MRZ lines.
        return: A dictionary containing decoded fields.
        """
        if not mrz_lines or len(mrz_lines) != 2:
            raise ValueError("Invalid MRZ input; two lines required.")

        # Example return logic
        decoded_data = {
            "passport_type": mrz_lines[0][0],
            "issuing_country": mrz_lines[0][2:5],
            "holder_name": mrz_lines[0][5:].replace("<", " ").strip(),
            "passport_number": mrz_lines[1][0:9],
            "passport_number_check_digit": mrz_lines[1][9],
            "country_code": mrz_lines[1][10:13],
            "birth_date": mrz_lines[1][13:19],
            "birth_date_check_digit": mrz_lines[1][19],
            "gender": mrz_lines[1][20],
            "expiration_date": mrz_lines[1][21:27],
            "expiration_date_check_digit": mrz_lines[1][27],
            "personal_number": mrz_lines[1][28:42],
            "personal_number_check_digit": mrz_lines[1][42]
        }
        return decoded_data

    def encode_mrz(self, fields):
        """
        Encodes travel document information into MRZ format.

        fields: A dictionary containing fields.
        return: A list of two strings representing the encoded MRZ lines.
        """

        # Example encoding logic
        # Encode fields into MRZ format
        # First line for passport type and issuing country
        # Second line for holder name etc..
        return [line1, line2]

    def calculate_check_digit(field):
        """
        Calculates the check digit for a given field.

        field: The field string for which to calculate the check digit.
        return: The check digit as a string.
        """
        mapping = {}
        for i, char in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<"):
            mapping[char] = i

        weights = [7, 3, 1]
        total = 0

        for index, char in enumerate(field):
            value = mapping[char]
            weight = weights[index % 3]
            total += value * weight

        check_digit = total % 10

        # Return the check digit as a string
        return str(check_digit)

    def validate_check_digits(decoded_data):
        """
        Validates the check digits for the fields.

        decoded_data: A dictionary containing fields and their check digits.
        return: A list of mismatched fields, if any.
        """
        fields_to_validate = ["passport_number", "birth_date", "expiration_date", "personal_number"]
        mismatches = []

        for field in fields_to_validate:
            field_value = decoded_data.get(field, "")
            expected_digit = decoded_data.get(f"{field}_check_digit", "")
            calculated_digit = calculate_check_digit(field_value)

            if calculated_digit != expected_digit:
                mismatches.append({
                    "field": field,
                    "expected": expected_digit,
                    "calculated": calculated_digit
                })

        return mismatches


if __name__ == "__main__":
    processor = MRTDProcessor()

    # Decode MRZ
    decoded_fields = processor.decode_mrz(mrz_lines)
    print("Decoded Fields:", decoded_fields)

    # Validate Check Digits
    mismatches = processor.validate_check_digits(decoded_fields)
    print("Check Digit Validation Mismatches:", mismatches)

    # Encode MRZ
    encoded_mrz = processor.encode_mrz(decoded_fields)
    print("Encoded MRZ Lines:", encoded_mrz)
