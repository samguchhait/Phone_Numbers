from argparse import ArgumentParser
import re
import sys

LETTER_TO_NUMBER = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': '9'
}

class PhoneNumber:
    """  A class that represents a phone numbers from the North American
    numbering plan.

    Attributes:
        area_code (int or str): first 3 characters in the number
        exchange_code (int or str): middle 3 characters in the number
        line_number (int or str): last 4 characters in the number

    Methods:
        __init__(self, phone_number): Initializes a PhoneNumber object with a
            given phone number.
        __int__(self): Converts the PhoneNumber object to an integer based on
            its components.
        __repr__(self): Returns a string representation of the PhoneNumber object
            for debugging.
        __str__(self): Returns a formatted string representation of the
            PhoneNumber object.
        __lt__(self, other): Compares two PhoneNumber objects based on their
            numerical values.
    """

    def __init__(self, phone_number):
        """ Initializes a PhoneNumber object with a given phone number.

        Args:
            phone_number (str or int): The input phone number to be processed.

        Side effects:
            Sets the instance variables area_code, exchange_code, and line_number.

        Raises:
            TypeError: Raises an error if it is not a string or an integer.
            ValueError: Raises an error if the phone_number is invalid.

        """
        if isinstance(phone_number, str):
            digits = re.sub(r'(?i)\D',
                            lambda match: LETTER_TO_NUMBER.get(match[0].upper(), "")
                            , phone_number)
        elif isinstance(phone_number, int):
            digits = str(phone_number)
        else:
            raise TypeError

        regex1 = r'^1?([2-9](?:[02-8]\d|1[02-8])[2-9](?:[02-8]\d|1[02-8])\d{4})$'
        match = re.search(regex1, digits)
        if not match:
            raise ValueError
        self.phone_number = match[1]
        self.area_code = self.phone_number[:3]
        self.exchange_code = self.phone_number[3:6]
        self.line_number = self.phone_number[6:]

    def __int__(self):
        """Returns a phone number as an integer"""
        return int(self.phone_number)

    def __repr__(self):
        """Returns the formal representation of a phone number"""
        return f"PhoneNumber('{self.phone_number}')"

    def __str__(self):
        """Returns the informal string representation of a phone number"""
        return f"({self.area_code}) {self.exchange_code}-{self.line_number}"

    def __lt__(self, other):
        """ Compares two phone numbers and returns True or False"""
        return self.phone_number < other.phone_number
def read_numbers(filepath):
    """Extracts the name and corresponding phone number from a file.
    Args:
        filepath (str): Path to a file.
    Returns:
        list of tuples: A list of tuples (name, PhoneNumber) sorted in ascending order.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        phone_numbers = []
        for line in f:
            name, number = line.strip().split('\t')
            try:
                phone_obj = PhoneNumber(number)
                phone_numbers.append((name, phone_obj))
            except ValueError:
                pass

    phone_numbers.sort(key=lambda x: int(x[1]))
    return phone_numbers

def main(path):
    """Read data from path and print results.

    Args:
        path (str): path to a text file. Each line in the file should consist of
            a name, a tab character, and a phone number.

    Side effects:
        Writes to stdout.
    """
    for name, number in read_numbers(path):
        print(f"{number}\t{name}")
def parse_args(arglist):
    """Parse command-line arguments.

    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.

    Args:
        arglist (list of str): a list of command-line arguments to parse.

    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of names and numbers")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)