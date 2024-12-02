# SSW567-FinalProject

# Machine-Readable Travel Document (MRTD) System

## Project Description
This project implements a system to process Machine Readable Travel Documents (MRTDs), ensuring global interoperability and accurate data handling. The system includes functionalities for:
- Scanning the Machine Readable Zone (MRZ) of travel documents
- Decoding MRZ data into structured fields
- Encoding structured fields back into MRZ format
- Validating fields using check digits to ensure data integrity
- Reporting mismatches for incorrect fields
This project was developed as part of SSW567: Software Testing, Quality Assurance, and Maintenance at Stevens Institute of Technology. The project showcases a comprehensive approach to software testing and quality assurance principles, connecting different testing topics learned throughout the semester.

---

## Features
- MRZ Scanning: Simulates reading the MRZ from travel documents
- Data Decoding: Converts MRZ strings into structured fields like passport number, issuing country, and holder's name
- Data Encoding: Generates MRZ strings from structured data fields
- Check Digit Validation: Validates MRZ fields using ICAO-compliant check digit algorithms
- Mismatch Reporting: Identifies discrepancies between fields and their respective check digits

---

## Requirements
- **MRZ Scanning**  
  Simulate a hardware scanner to extract two strings from the MRZ. A placeholder method is defined as the hardware implementation is out of scope.

- **MRZ Decoding and Encoding**  
  - Decode MRZ strings into fields and check digits.  
  - Encode fields into MRZ strings using predefined formats.

- **Check Digit Validation**  
  - Multiply each character's numeric value with a fixed weighting sequence (7, 3, 1).  
  - Calculate the modulus-10 remainder to determine the check digit.  

- **Mismatch Detection**  
  Report field mismatches between extracted data and computed check digits.

---

##Technologies Used
- Programming Language: Python 3.7.15
- Testing Tools:
   - unittest for unit tests
  - coverage.py for code coverage analysis
  - MutPy for mutation testing
- Development Tools: GitHub for version control

---

## Project Components
1. **Kickoff & Planning**  
   Initial project setup, requirement analysis, and task breakdown.

2. **Requirement Testing**  
   Validate system requirements for accuracy and completeness.

3. **Unit Testing**  
   Develop unit tests for individual components, ensuring functionality and correctness.

4. **Performance Testing**  
   Assess system performance under various conditions, focusing on reliability and efficiency.

5. **Test Planning**  
   Create a detailed test plan to guide the verification process.

---

## Deliverables
- Unit Tests: Comprehensive test cases for all functionalities
- Coverage Report: Code coverage > 90%
- Mutation Testing: Identified and resolved uncovered scenarios
- Performance Analysis: Execution times for processing datasets of increasing sizes
