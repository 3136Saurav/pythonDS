from Stacks_Python import Stack

def convertDecimal2Binary(n):
    remStack = Stack()
    while n>0:
        rem = n%2
        remStack.push(rem)
        n = n//2

    result = ''
    while not remStack.isEmpty():
        result += str(remStack.pop())

    return result


if __name__ == '__main__':
    n = int(input())
    result = convert2Binary(n)
    print("Result --> ", result)
