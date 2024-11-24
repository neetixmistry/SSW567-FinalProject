# SSW567-FinalProject

# Machine-Readable Travel Document (MRTD) System

## Overview
This project implements a system to read and verify the Machine-Readable Zone (MRZ) of travel documents, such as passports, to ensure global interoperability through optical character recognition (OCR) and field validation. The system is designed as part of the **SSW567: Software Testing, Quality Assurance, and Maintenance** course at Stevens Institute of Technology.

The project showcases a comprehensive approach to software testing and quality assurance principles, connecting different testing topics learned throughout the semester.

---

## Features
1. **MRZ Scanning and Decoding**  
   - Extracts MRZ information from a travel document.
   - Decodes MRZ strings into individual fields such as passport type, country code, passport number, and more.

2. **Check Digit Validation**  
   - Validates MRZ fields against their respective check digits using a weighted modulus algorithm.

3. **Field Mismatch Reporting**  
   - Identifies and reports discrepancies between MRZ fields and check digits for error detection.

4. **MRZ Encoding**  
   - Converts travel document information from a database into MRZ string format.

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


