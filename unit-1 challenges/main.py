"""write a python program to find the factorial using
recursion function"""
def rec_fact(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return n * (rec_fact(n - 1))


number = int(input("ENTER A NUMBER:"))
res = rec_fact(number)
print(
  "THE FACTORIAL OF",
  number,
  "IS",
  res,
)