from linkedstack import LinkedStack


def EvaluatePostfix(str):
    stack = LinkedStack()
    for char in str:
        if char == '+':
            stack.push(stack.pop() + stack.pop())
        elif char == '-':
            stack.push(-stack.pop() + stack.pop())
        elif char == '*':
            stack.push(stack.pop() * stack.pop())
        elif char == '/':
            a = stack.pop()
            b = stack.pop()
            stack.push(b / a)
        else:
            stack.push(int(char))
    return stack.pop()


if __name__ == '__main__':
    str = '32+1/3*'
    print(EvaluatePostfix(str))
