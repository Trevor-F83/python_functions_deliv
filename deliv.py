def sum_to(n):
  sum = 0
  for num in range(0, n+1):
    sum = sum+num
  return(sum)

total = sum_to(12)
print(total)

# exercise 2

def largest(x):
  print(max(x))

largest([2, 5, 6, 8, 10])

# exercise 3

def occurences(x, y):
  z = x.count(y)
  print(z)
occurences('fleep flop', 'e')

# exercise 4

def product(*args):
  for arg in args:
    return arg * args
    print(args)
product(5,5)
