#!/usr/bin/python

import sys
rps = ['rock','paper','scissors']
rps_helper = []
def rock_paper_scissors_helper(m):
  if m == 0:
    return []
  else:
    sorted = True
    while sorted:
      for item in range(len(rps)):
        rps_helper.append([rps[item]] * m) 
        sorted = False  
      print(rps_helper)
      return rps_helper

def rock_paper_scissors(n):
  if n <= 0:
    return []
  else:   
    rock_paper_scissors_helper(n)
    return rock_paper_scissors(n-1)
  
rock_paper_scissors(2)
  
        


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')