#!/usr/bin/env python

import argparse
from random import randint

def run_exp():
  door_car = randint(1,3)
  door_chosen = randint(1,3)
  door_remove_candidates = list(set([1,2,3])-set([door_car, door_chosen]))
  door_remove = door_remove_candidates[randint(0,len(door_remove_candidates)-1)%len(door_remove_candidates)]
  door_final = list(set([1,2,3])-set([door_chosen, door_remove]))[0]
  return door_final == door_car

# command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_exp',  type=int, help='number of experiments to run', default=1000000)
args = parser.parse_args()

success = 0
for i in range(args.num_exp):
  success += run_exp()
print 'number of winning out of '+str(args.num_exp)+' tries is '+str(success)
print 'win rate: '+str(float(success)/args.num_exp)
