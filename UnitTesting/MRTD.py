# MRTD.py

class MRTDProcessor:
    def __init__(self):
        pass

    def scan_mrz(self):
        """
        simulates scanning the MRZ (Machine Readable Zone) from a travel document.
        """
        pass # pragma: no cover

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
            "last_name": mrz_lines[0][5:].replace("<", " ").strip().split(" ",1)[0],
            "given_name": (mrz_lines[0][5:].replace("<", " ").strip().split(" ",1)[1]).strip(),
            "passport_number": mrz_lines[1][0:9],
            "passport_number_check_digit": mrz_lines[1][9],
            "country_code": mrz_lines[1][10:13],
            "birth_date": mrz_lines[1][13:19],
            "birth_date_check_digit": mrz_lines[1][19],
            "sex": mrz_lines[1][20],
            "expiration_date": mrz_lines[1][21:27],
            "expiration_date_check_digit": mrz_lines[1][27],
            "personal_number": mrz_lines[1][28:42].rstrip("<"),
            "personal_number_check_digit": mrz_lines[1][43]
        }
        return decoded_data

    def database_query(self):
        """
        simulates query froma  database to get feilds of information
        """
        pass # pragma: no cover

    def encode_mrz(self, fields):
        """
        Encodes travel document information into MRZ format.

        fields: A dictionary containing fields.
        return: A list of two strings representing the encoded MRZ lines.
        """
        line1 = fields["passport_type"] + "<" + fields["issuing_country"] + fields["last_name"] + "<<" + fields["given_name"].replace(" ", "<")
        line1 += (44 - len(line1)) * "<"
        line2 = fields["passport_number"] + self.calculate_check_digit(fields["passport_number"]) + fields["country_code"] \
        + fields["birth_date"] + self.calculate_check_digit(fields["birth_date"]) + fields["sex"] + fields["expiration_date"] \
        + self.calculate_check_digit(fields["expiration_date"]) + fields["personal_number"]
        line2 += (43 - len(line2)) * "<"
        line2 += self.calculate_check_digit( fields["personal_number"])
        return [line1, line2] 

    def calculate_check_digit(self, field):
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

    def validate_check_digits(self, decoded_data):
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
            calculated_digit = self.calculate_check_digit(field_value)

            if calculated_digit != expected_digit:
                mismatches.append({
                    "field": field,
                    "expected": expected_digit,
                    "calculated": calculated_digit
                })

        return mismatches


if __name__ == "__main__":
    processor = MRTDProcessor()
    mrz_lines = ["P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<","W620126G54CIV5910106F9707302AJ010215I<<<<<<6"]
    # Decode MRZ
    decoded_fields = processor.decode_mrz(mrz_lines)
    print("Decoded Fields:", decoded_fields)

    # Validate Check Digits
    mismatches = processor.validate_check_digits(decoded_fields)
    print("Check Digit Validation Mismatches:", mismatches)

    #Encode MRZ
    encoded_mrz = processor.encode_mrz(decoded_fields)
    print("Encoded MRZ Lines:", encoded_mrz)
