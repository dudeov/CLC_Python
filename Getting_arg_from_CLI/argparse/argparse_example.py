#!/usr/bin/env python3

import argparse

# DO NOT EDIT BELOW HERE:
# Collect User input:
def check_cli_args():
    parser = argparse.ArgumentParser(
        description="Put smth here")

    parser.add_argument(
        '-c', '--config', type=str, help='Config file to be converted (REQUIRED)', required=True
    )

    args = parser.parse_args()
    return args
    
args = check_cli_args()
print("You enetered:%s " % (args))