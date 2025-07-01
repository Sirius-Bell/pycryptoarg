import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="simple script to encrypt a file or message"
    )
    parser.add_argument("-d", "--debug", action="store_true", help="turn on debug mode")
    parser.add_argument(
        "-f", "--file", action="store", help="the name of the file to encrypt"
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        default=sys.stdout,
        help="the name of the output file",
    )

    args = parser.parse_args()
