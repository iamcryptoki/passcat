#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Passcat lets you generate cryptographically secure, memorable passphrases.

Usage:
    passcat [COUNT] [--file=f] [--help] [--list] [--version] [--wordlist=w]

Options:
    -f --file=f               Specify the path to an alternate wordlist.
    -h --help                 Show this message.
    -l --list                 Show available wordlists.
    -v --version              Show version.
    -w --wordlist=w           Specify a wordlist. [default: eff]
"""

import os
import sys
import docopt

from . import __version__
from secrets import choice

_dir = os.path.dirname(os.path.abspath(__file__))

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
    return ' '.join(choice(words) for i in range(count))

def main():
    args = docopt.docopt(__doc__, version=__version__)

    if args['--list']:
        print('\n'.join(sorted(wordlists())))
        sys.exit(0)

    path = args['--file']
    if path is None:
        path = '%s/wordlists/%s.txt' % (_dir, args['--wordlist'].lower())

    try:
        with open(path) as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print("File not found. Please input the path of an existing "
              "file or use the '-l' flag to show available wordlists.")
        sys.exit(1)

    count = args['COUNT'] if args['COUNT'] is not None else 6
    if not str(count).isdigit():
        print("Please input a valid number.")
        sys.exit(1)

    passphrase = generate(words, int(count))
    print(passphrase)

if __name__ == '__main__':
    main()
