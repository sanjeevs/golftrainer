import argparse
import os
import csv

from golftrainer import factory

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Load info from database")

    parser.add_argument("json", type=str, help="Swing state in json format")
    return parser


def main():
    opt = create_parser().parse_args()
    with open(opt.json, 'r') as file:
        data = file.read()
    gd = factory.create_golf_data(data)
    print(f"Found in each frame {len(gd.mp_result[0])} mp_entries")

if __name__ == "__main__":
    main()