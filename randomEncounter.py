#!/usr/local/bin/python3

import sys
import getopt
import json
import re
import random
from colorcodes import clr
from enctable import enctabledict


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
#  print("Rolling " + str(n) + "d" + str(d) + (" + ","")[neg] + str(a))

  s = 0
  for x in range(0, n):
    s = s + random.randint(1,d)
  s = s + a
  return clr.YELLOW + clr.BOLD + str(s) + clr.ENDC + clr.GREEN

def printEnc(name):
  f = open('randomEncounters.json')
  encounters = json.load(f)
  print(clr.BOLD + clr.LIGHTGRAY + clr.BG_BLUE + name + clr.ENDC)
  for x in encounters["encounters"]:
      if x["name"] == name:
        text = x["text"]
        text = text.replace("\\n", "\n\n")
        text = re.sub('(\d+)d(\d+)([\+|-]\d+)?', rollDice, text)
        print(clr.GREEN + text + clr.ENDC)
        print(clr.YELLOW + x["treasure"] + clr.ENDC)
        for y in x["creatures"]:
          print(clr.RED + y + clr.ENDC)

def main(argv):
  terrain = ""
  try:
    opts, args = getopt.getopt(argv,"ht:",["terrain="])
  except getopt.GetoptError:
    print('randomEncounter.py -t <terrain>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print(f'''
randomEncounter.py -t <terrain>'

Valid terrains:
  Forest
  Grassland
  Hills
  Mountains
  Road
  Sea
  Tundra
''')
      sys.exit()
    elif opt in ("-t", "--terrain"):
      terrain = arg
  terrain = terrain.lower()
  print('Terrain: ' + terrain)


  tableroll = random.randint(1,100)
  print("Roll:", tableroll)
  for rng, enc in enctabledict.enctable[terrain].items():
    low,high = rng.split("-")
    if int(low) <= tableroll <= int(high):
      printEnc(enc) 

if __name__ == "__main__":
   main(sys.argv[1:])
