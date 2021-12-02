default_operators = {
    ""
}

"""
Use these'+','-','*' and'/' operators and the given four numbers to calculate all possible expressions for 24
"""
def calc24(arr):
  if len(arr) != 4:
    raise Exception("Input arr must be 4")
  
  operators = ["+", "-", "*", "/"]
  return create_expr(arr, operators)

"""
Extended calc 24

Support more than 4 numbers and more than 4 operators
"""
def exc24(nums, operators: map(str, int)):
    pass

"""
Create all expressions and check them

Now 'ops' and 'nums' are not supported to be others
"""
def create_expr(nums, ops, expr_max_len = 7, expr = [], result = []):
  expr_len = len(expr)
  if expr_len == expr_max_len:
    if eval_expr(expr) == 24:
      result.append(expr)

  elif expr_len % 2 == 0:
    for i in range(0, len(nums)):
      new_nums, num = nm_pop(nums, i)
      create_expr(new_nums, ops, expr + [num], result)
  else:
    for i in range(0, 3):
      create_expr(nums, ops, expr + [ops[i]], result)
  
  return result

"""
No modify pop

this pop method won't modify the original list.
return a tuple with the first element is the new list and the second element is the element that you poped
"""
def nm_pop(list, index):
  return (list[:index] + list[index + 1:], list[index])

def eval_expr(expr):
  result = expr[0]
  for i in range(1, 7, 2):
    op = expr[i]
    num = expr[i + 1]

    if op == "+":
      result += num
    elif op == "-":
      result -= num
    elif op == "*":
      result *= num
    else: 
      result /= num
  
  return result

"""
Perttify the solutions that generates from calc24
"""
def perttify_solutions(solutions, no_solution="No solutions find! :("):
  solutions_len = len(solutions)

  if solutions_len == 0:
    return [no_solution]

  lines = []
  for i in range(0, solutions_len):
    str = ""
    for c in range(0, 7):
      str = f"{str}{solutions[i][c]}"
    lines.append(f"{str}=24")
  return lines

"""
CLI tool entry point
"""
def main():
  import time

  print("Tell me the numbers. Use ',' to seperate each. Any spaces will be trim")
  
  input_raw = input("Input: ").strip().split(",")
  input_trim = []
  for i in range(0, len(input_raw)):
    input_trim.append(int(input_raw[i].strip()))
  if len(input_trim) != 4:
    print("You need input only 4 numbers")
    return main()

  start_time = time.time_ns() // 10**6
  solutions = perttify_solutions(calc24(input_trim))
  solutions_len = len(solutions)
  print(f"Done! Time elapsed: {(time.time_ns() // 10**6) - start_time}ms and {solutions_len} of solution(s) find")
  for i in range(0, solutions_len):
    print(solutions[i])

if __name__ == "__main__":
  main()