def calculate(sentence):
    stack = []
    operator = "+-*/"

    for char in sentence:
        if char == " ":
            pass
        elif char not in operator:
            stack.append(int(char))
        elif char == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif char == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(a - b)
        elif char == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif char == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(a // b)

    return stack.pop()
print(calculate("2 3 + 5 *"))
print(calculate("4 2 / 3 - 2 *"))
print(calculate("4 2 3 + *"))

# 이 코드가 정확도가 떨어질것 같은데 어떻게 보완해야할지 잘 모르겠습니다..리뷰 부탁드립니다!!ㅠ
