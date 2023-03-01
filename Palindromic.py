from linkedstack import LinkedStack


def Palindrome(str):
    stack = LinkedStack()
    for char in str:
        stack.push(char)
    for ele in str:
        if stack.pop() != ele:
            return False
    return True


if __name__ == '__main__':
    str = input('Enter a string to check weather it is Palindrome or not ?')
    print(Palindrome(str))
