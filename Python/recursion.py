def recursion_without_returning_function_call(number):
  if number == 0:
    return 'Doesn\'t matter what value you return, this is an exit criteria to prevent infinite loop if you don\'t return function call'

  recursion_without_returning_function_call(number - 1)

  return 'Return something irrelevant here'


def recursion_with_returning_function_call(number):
  if number == 0:
    return 'Return base value to the first function call'

  return recursion_with_returning_function_call(number - 1)


def recursion_example1(number):
  if number == 0:
    return 'Reach the base, doesn\'t matter what we return too'

  if number == 3:
    return 'Return the answer, yes contains 3'

  return recursion_example1(number - 1)


def recursion_example2(number):
  if number == 0:
    return 'Reach the base, no doesn`t contain 6'

  if number == 6:
    return 'Return the answer, yes contains 6'

  return recursion_example2(number - 1)


def recursion_example3(number, queue):
  if number == 0:
    return queue

  queue.append(number)

  return recursion_example3(number - 1, queue)


print '1. If you don\'t return function call, what base returns doesn\'t matter:', recursion_without_returning_function_call(5)
print '2. If you return function call, what base returns does matter:', recursion_with_returning_function_call(5)
print '3. Check if decremented number 5 contains 3:', recursion_example1(5)
print '4. Check if decremented number 5 contains 6:', recursion_example2(5)
print '5. Store decrement number in a queue: Return a queue;', recursion_example3(5, [])

# $ python recursion.py
# 1. If you don't return function call, what base returns doesn't matter: Return something irrelevant here
# 2. If you return function call, what base returns does matter: Return base value to the first function call
# 3. Check if decremented number 5 contains 3: Return the answer, yes contains 3
# 4. Check if decremented number 5 contains 6: Reach the base, no doesn`t contain 6
# 5. Store decrement number in a queue: Return a queue; [5, 4, 3, 2, 1]
