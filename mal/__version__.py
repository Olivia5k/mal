"""
Quick and dirty git-tag based automatic versioning.

Mostly a proof of concept. Might spook up in non-standard scenarios.

"""


import sys
import subprocess as sp
import logging
import time


try:
    cmd = 'git describe --tags --always --dirty'.split(' ')
    proc = sp.Popen(cmd, stdout=sp.PIPE)
    out = proc.communicate()[0]

    if sys.version_info >= (3, ):
        out = out.decode()

    version = out.strip()

except Exception as e:
    logging.exception('Shit happened. Version unknown.')
    time.sleep(3)

    version = 'unknown'
