def precedence(op):
    if op == '^':
        return 3
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []   # operator stack
    result = ""  # postfix result

    for ch in expression:
        # If operand → add to result
        if ch.isalnum():
            result += ch
        # If '(' → push to stack
        elif ch == '(':
            stack.append(ch)
        # If ')' → pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # remove '('
        # If operator
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                result += stack.pop()
            stack.append(ch)

    # Pop remaining operators
    while stack:
