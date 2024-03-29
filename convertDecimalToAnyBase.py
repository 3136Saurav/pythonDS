from Stacks_Python import Stack

def convert_decimal_to_any_base(n, b):
    remStack = Stack()
    digits = '0123456789ABCDEF'

    while n>0:
        rem = n%b
        remStack.push(rem)
        n = n//b

    result = ''
    while not remStack.isEmpty():
        result += (digits[remStack.pop()])

    return result

if __name__ == '__main__':
    n = int(input('Enter any number: '))
    b = int(input('Enter any base: '))
    result = convert_decimal_to_any_base(n,b)
    print('Result --> ',result)
