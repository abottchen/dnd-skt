#!/usr/local/bin/python3

import sys
import getopt
import json
import re
import random
from colorcodes import clr
from enctable import enctabledict


def rollDice(dice):
  regex = re.match('(\d+)d(\d+)([\+|-]\d+)?', dice)
  n = int(regex.group(1))
  d = int(regex.group(2))
  neg = False
  if regex.group(3):
    if regex.group(3)[0:1] == "-":
      neg = True
      a = int(regex.group(3))
    else:
      a = int(regex.group(3)[1:])
  else:
    a = 0
  #print("Rolling " + str(n) + "d" + str(d) + (" + ","")[neg] + str(a))

  s = 0
  for x in range(0, n):
    s = s + random.randint(1,d)
  s = s + a
  return s

def main(argv):
  temp = rollDice('1d20')
  wind = rollDice('1d20')
  precip = rollDice('1d20')
  
  if temp <= 14:
      tempstr = "normal for the season"
  elif temp <=17:
      tempstr = str(rollDice('1d4') * 10) + " degrees colder than normal"
  else:
      tempstr = str(rollDice('1d4') * 10) + " degrees warmer than normal"

  if wind <= 12:
      windstr = "no wind"
  elif wind <=17:
      windstr = "light winds"
  else:
      windstr = "strong winds"

  if precip <= 12:
      precipstr = "no precipitation"
  elif precip <=17:
      precipstr = "light precipitation"
  else:
      precipstr = "strong precipitation"

  print("Today it is " + tempstr + " with " + windstr + " and " + precipstr)

if __name__ == "__main__":
   main(sys.argv[1:])
