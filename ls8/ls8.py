#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# try:
cpu.load(sys.argv[1])
cpu.run()
# except IndexError:
#     print('No program path provided')
