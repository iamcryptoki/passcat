#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from argparse import ArgumentParser
from random import SystemRandom

_dir = os.path.dirname(os.path.abspath(__file__))

def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument('-c', '--count', default=8, help="Number of words to use in the passphrase.")
    parser.add_argument('-f', '--file', default=None, help="Path to an alternate wordlist.")
    parser.add_argument('-l', '--list', action='store_true', help="Available wordlists.")
    parser.add_argument('-w', '--wordlist', default='eff', help="Wordlist to use.")
    return parser.parse_args()

def wordlists():
    """
    List available wordlists.
    """
    return [a.replace('.txt', '').capitalize()
            for a in os.listdir(_dir+'/wordlists/')
            if a.endswith('.txt')]

def generate(words, count):
    """
    Generate passphrase.
    """
    return ' '.join(SystemRandom().sample(words, count))

def main():
    args = parse_arguments()
    path = args.file
    if args.list:
        print('\n'.join(sorted(wordlists())))
        sys.exit()
    if path is None:
        path = '%s/wordlists/%s.txt' % (_dir, args.wordlist.lower())
    try:
        with open(path) as f:
            words = f.read().splitlines()
            f.close()
    except FileNotFoundError:
        print("Error: File not found. Please input the path of an existing file "
                "or use the '-l' flag to show available wordlists.")
        sys.exit()

    if not str(args.count).isdigit():
        print("Error: Please input a valid number.")
        sys.exit()

    passphrase = generate(words, int(args.count))
    print(passphrase)

if __name__ == '__main__':
    main()
