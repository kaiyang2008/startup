#!/usr/bin/python3

import sys
sys.path.append("~/work/python/begin_python/1")
from lib.Person import Person

foo=Person()
foo.greet()

foo.set_name("snps")

foo.greet()
