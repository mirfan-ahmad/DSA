from ArrayStack import ArrayStack


def PostfixEvaluator(exp):
    stack = ArrayStack(100)
    for ele in exp:
        if ele == '+':
            stack.push(stack.pop() + stack.pop())
        elif ele == '-':
            a, b = stack.pop(), stack.pop()
            stack.push(b - a)
        elif ele == '*':
            stack.push(stack.pop() * stack.pop())
        elif ele == '/':
            a, b = stack.pop(), stack.pop()
            stack.push(b / a)
        else:
            stack.push(int(ele))
    return stack.pop()


if __name__ == '__main__':
    expression = input('Enter any postfix exp to evaluate? ')
    print(PostfixEvaluator(expression))
