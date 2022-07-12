def isValid(s):
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']  # 为了防止stack.pop() 报错，取巧
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1


if __name__ == '__main__':
    s = "[]{}{{[]}[]}"
    x = isValid(s)
    print(x)
