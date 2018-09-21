class Solution(object):
    def __init__(self):
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

    def calculator(self, express):
        operater_stack = []
        middle_stack = []
        for el in express:
            if el.isdigit():
                middle_stack.append(el)
            elif el == '(':
                operater_stack.append(el)
            elif el == ')':
                op = operater_stack.pop()
                while op != '(':
                    if op != '(':
                        middle_stack.append(op)
                    op = operater_stack.pop()
            else:
                if not operater_stack:
                    operater_stack.append(el)
                else:
                    if operater_stack[-1] != '(' and self.priority[el] < self.priority[operater_stack[-1]]:
                        op = operater_stack.pop()
                        while op != '(':
                            middle_stack.append(op)
                            if operater_stack:
                                op = operater_stack.pop()
                            else:
                                break
                        operater_stack.append(el)
                    else:
                        operater_stack.append(el)
        while operater_stack:
            op = operater_stack.pop()
            middle_stack.append(op)
        return ''.join(middle_stack)


ins = Solution()
# a = '4+5*6-3'
# print(ins.calculator(a))
b = '(4+5)*(6-3)'
print(ins.calculator(b))


