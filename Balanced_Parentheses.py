from Stacks_Python import Stack    

def parChecker(expr):
    s = Stack()
    index = 0
    balanced = True
    while index < len(expr) and balanced:
        symbol = expr[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    return balanced   # ((())())

if __name__ == '__main__':
    s = input()
    t = parChecker(s)
    print(t)
