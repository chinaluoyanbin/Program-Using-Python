def bracketsBalance(s):
    stk = []
    for ch in s:
        if ch in ['[', '(']:
            stk.append(ch)
        if ch in [']', ')']:
            if len(stk) == 0:
                return False
            chFromStack = stk.pop()
            if (ch == ')' and chFromStack != '(') or (ch == ']' and chFromStack != '['):
                return False
    return len(stk) == 0


s = '[()]'
print(bracketsBalance(s))
