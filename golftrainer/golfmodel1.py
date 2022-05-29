"""Golf trainer script to analze a golf swing."""

import argparse
import os.path
import cv2


def create_parser():
    """"Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Golf trainer to analyze a golf swing video."
    )
    parser.add_argument("srcdir", type=str, help="Frame or dir holding all the json files.")
    return parser


def main():
    """Main program"""
    opt = create_parser().parse_args()