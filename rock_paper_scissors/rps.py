#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock','paper','scissors']
  plays = []
  def rock_paper_scissors_helper(options,n):
    if n == 0:
      plays.append(options)
    else:
      for item in rps:
        rock_paper_scissors_helper(options + [item], n - 1 )
  rock_paper_scissors_helper([],n)
  print(plays)
  return plays
rock_paper_scissors(2) 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')