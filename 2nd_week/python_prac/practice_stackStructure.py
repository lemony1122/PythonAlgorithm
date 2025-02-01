def test_problem_stack(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack: # if len(stack_==0:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack