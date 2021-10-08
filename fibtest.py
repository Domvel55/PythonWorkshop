"""

Fibonacci calculator
By: Dominick Velardo

"""


ancestor, predecessor = 1, 1

# Returns the top number in the fib sequence after the number given
def fib(top_num: int):
    global ancestor, predecessor

    sequence = [1, 1]
    result : int = 0
    while result < top_num:
        result = ancestor + predecessor

        if result > 100:
            print('Too high, try again!')
            break

        predecessor = ancestor
        ancestor = result
        sequence.append(result)

    else: print('Completed')

    ancestor, predecessor = 1, 1
    return sequence


if __name__ == '__main__':
    print(fib(53), '\n')
    print(fib(200))