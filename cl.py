#!/usr/bin/python3

import sys
import random

rand_arg_num = random.randint(1,len(sys.argv) - 1)
print (sys.argv[rand_arg_num])
