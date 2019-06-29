#!/usr/local/bin/python3

import sys
import getopt
import json
import re
import random
from colorcodes import clr
from giantbagitems import giantbagdict


def rollDice(var):
  n = int(var.group(1))
  d = int(var.group(2))
  neg = False
  if var.group(3):
    if var.group(3)[0:1] == "-":
      neg = True
      a = int(var.group(3))
    else:
      a = int(var.group(3)[1:])
  else:
    a = 0

  s = 0
  for x in range(0, n):
    s = s + random.randint(1,d)
  s = s + a
  return clr.YELLOW + clr.BOLD + str(s) + clr.ENDC + clr.GREEN

def printItem(name):
  name = re.sub('(\d+)d(\d+)([\+|-]\d+)?', rollDice, name)
  print(clr.GREEN + name + clr.ENDC)

def main(argv):
  number = 1
  try:
    opts, args = getopt.getopt(argv,"hn:",["number="])
  except getopt.GetoptError:
    print('giantBag.py -n <number of items>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print(f'''
giantBag.py -n <number of items>'
''')
      sys.exit()
    elif opt in ("-n", "--number"):
      number = int(arg)
  print('Number of items: ' + str(number))


  for i in range(0,number):
    tableroll = random.randint(1,100)
    print("Roll:", tableroll)
    for rng, item in giantbagdict.bagtable.items():
      low,high = rng.split("-")
      if int(low) <= tableroll <= int(high):
        printItem(item) 

if __name__ == "__main__":
   main(sys.argv[1:])
