from Stacks_Python import Stack

def general_parChecker(expr):
    s = Stack()
    balanced = True
    index = 0
    while index<len(expr) and balanced:
        symbol = expr[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True

    return False

def matches(open, close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)

if __name__ == '__main__':
    s = input()
    t = general_parChecker(s)
    print(t)
