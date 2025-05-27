# Phone Numbers

A command-line Python program that reads names and phone numbers from a file, validates and formats the numbers using the North American Numbering Plan (NANP), and prints them in sorted order.

## Features
- Converts letters in phone numbers to their numeric equivalent (e.g., `1-800-FLOWERS` to `1-800-356-9377`). 
- Supports optional leading `1` for U.S. country code.
- Validates phone numbers using NANP rules.
- Skips invalid or malformed phone numbers.
- Sorts entries by phone number.
- Outputs formatted phone numbers as `(XXX) XXX-XXXX`.

## Input Format
The input file must contain one entry per line, with:
- A name
- A tab character (`\t`)
- A phone number

**Example:**
```
Alice\t1-800-FLOWERS
Bob\t(212) 555-7890
Charlie\t301.555.1234
```

## Output Format
The program prints valid phone numbers in this format, sorted numerically:

**Example Sorted:**
```
(212) 555-7890	Bob
(301) 555-1234	Charlie
(800) 356-9377	Alice
```


## How to Run

- Make sure you have Python 3.x installed.
- No external libraries required (only argparse, re, and sys).
- My program is designed to run from the terminal.
- To run it, open a terminal and ensure you are in the directory where your script and sample file are saved.


The examples below assume you are using macOS and your program is called `phone_numbers.py` and the input file is called `sample_phone_numbers.txt`.

If you are using Windows, replace `python3` with `python`.

### Command-line Argument to Run Program

The script prints cleaned, formatted, and sorted phone numbers to standard output: 

`python3 phone_numbers.py sample_phone_numbers.txt`
