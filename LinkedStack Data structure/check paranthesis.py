from linkedstack import LinkedStack


def BalanceParenthesis(str):
    stack = LinkedStack()
    dict = {'(': ')', '{': '}', '[': ']'}
    for char in str:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if dict[stack.top()] == char:
                stack.pop()
    if stack.isEmpty():
        return True
    return False


if __name__ == '__main__':
    str = '[{}]'
    print(BalanceParenthesis(str))
