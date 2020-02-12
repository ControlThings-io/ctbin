# Copyright (C) 2019  Justin Searle
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details at <http://www.gnu.org/licenses/>.

from ctui.application import Ctui
from ctui.types import *
import os
import string

myapp = Ctui()

myapp.name = 'ctbin'
myapp.version = '0.1'
myapp.description = 'Perform hex dump, diff, and analysis on bianry files'
myapp.prompt = 'ctbin> '
# myapp.help_text = 'Help menu for my ctui application'


# Example of a command with no arguments
@myapp.command
def do_ls():
    """Show files in current directory.""" 
    output_text = myapp.output_text      
    output_text += 'Directory contains:\n'
    for item in os.listdir():
        output_text += ' ' + item + '\n'
    return output_text


# Example of a command with 1 argument
@myapp.command
def do_cd(dir:str):
    """Change to a new direcotry.

    :PARAM dir: Directory to change into
    """
    try:
        os.chdir(dir)
    except:
        return False
    output_text = myapp.output_text          
    output_text = output_text + 'Directory changed to ' + dir + '\n'
    return output_text


@myapp.command
def do_strings(filename:str, min:int):
    """Find all printable ASCII characters in file.
    
    :PARAM filename: Name of file to use.
    :PARAM min: Minimum # of characters to show.
    """
    output_text = '\n'.join([string for string in strings(filename)])
    return output_text


@myapp.command
def do_xxd(filename:str):
    """Do hexdump of file.
    
    :PARAM filename: Name of file to use.
    """
    output_text = '\n'.join([string for string in strings(filename)])
    return output_text


def print_buf(counter, buf):
    buf2 = [('%02x' % ord(i)) for i in buf]
    count = '{0}: {1:<39}  {2}'.format(('%07x' % (counter * 16))
    hexout = ' '.join([''.join(buf2[i:i + 2]) for i in range(0, len(buf2), 2)])
    asciiout =  ''.join([c if c in string.printable[:-5] else '.' for c in buf]))


def process_xxd(file_path):
    with open(file_path, 'r') as f:
        counter = 0
        while True:
            buf = f.read(16)
            if not buf:
                break
            print_buf(counter, buf)
            counter += 1


# @myapp.command
# def do_open(filename:str):
#     """Open file to use with ctbin."""
#     with open(filename) as f:
#         # TODO: where to save in myapp?
    
#     output_text = f'{filename} opened'

#     # TODO: The followig section will be moved to a new dump or similar command
    
#     return output_text


def strings(filename, min=4):
    with open(filename, errors="ignore") as f:  # Python 3.x
    # with open(filename, "rb") as f:           # Python 2.x
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""
        if len(result) >= min:  # catch result at EOF
            yield result


myapp.run()
