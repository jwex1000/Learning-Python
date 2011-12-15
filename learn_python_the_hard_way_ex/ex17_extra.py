#!/usr/bin/env python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file).read()

output = open(to_file, 'w').write(input)

print "Alright, all done."

close(input)
close(output)

