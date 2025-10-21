import math

def main():
  x = 0
  step = (2 * math.pi) / 1000   

  print("x    sin(x)")
  while x <= 2 * math.pi:
    print(x, math.sin(x))
    x = x + step

main()
