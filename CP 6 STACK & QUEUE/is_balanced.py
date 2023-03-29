def is_balanced(input_str):
    s = list()

    for ch in input_str:
        if ch == '(' or ch == '{' or ch == '[':
            s.append(ch)
        else:
            if not s:
                return False
            b = s.pop()
            if b == '(':
                if ch != ')':
                    return False
            if b == '{':
                if ch != '}':
                    return False
                
            if b == '[':
                if ch != ']':
                    return False                
    return not s
    

if __name__ == "__main__":
    input_str = input()
    print(is_balanced(input_str))

    if is_balanced(input_str):
        print(input_str)
        print(input_str, "is balanced")
    else:
        print(input_str)
        print(input_str, "is not balanced")                