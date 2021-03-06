"""Command line parser for gendiff."""


import argparse

from gendiff import format


def formatter(name):
    """Choose a formatter function based on CL option input."""
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
        'Unknown formatter: {0}'.format(name),
    )


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f',
    '--format',
    metavar='FORMAT_NAME',
    help='set format of the output (default, json, or plain)',
    default=format.DEFAULT,
    # convert user input string into one of the formatter functions
    type=formatter,
    # argparse checks choices after the conversion, not before
    choices=(format.json, format.plain, format.default),
)
