#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = []
  for i in range(len(prices)-1):
    lhs = prices[:i]
    print(lhs)
    if len(lhs) > 1:
      profit = prices[i] - min(lhs)
      max_profit.append(profit)
  found_profit = max(max_profit)
  return found_profit
find_max_profit([10, 7, 5, 8, 11, 9])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))