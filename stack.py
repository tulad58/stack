import re


class Stack:

    def is_empty(self, stack):
        if stack:
            return True
        else:
            return False

    def push(self, object_element, new_list):
        new_list.append(object_element)

    def pop(self, stack):
        poped = stack.pop()
        return poped

    def peek(self, stack):
        return stack[-1]

    def size(self, stack):
        return len(stack)

    def if_balanced(self, stack):
        len_of_object = self.size(stack)
        if len_of_object % 2 != 0:
            return 'Несбалансированно'
        new_list_stack = []
        stack = [str(i) for i in stack]
        for i in range(len_of_object):
            braket = stack[i]
            if re.search(r"\(|\[|\{", braket):
                self.push(braket, new_list_stack)
            elif re.search(r"\)|\]|\}", braket) and self.is_empty(new_list_stack):
                last_new_list_stack = self.pop(new_list_stack)
                if braket == ')' and last_new_list_stack == '(':
                    continue
                elif braket == '}' and last_new_list_stack == '{':
                    continue
                elif braket == ']' and last_new_list_stack == '[':
                    continue
                else:
                    return 'Несбалансированно'
            else:
                return 'Несбалансированно'
        return 'Сбалансированно'

def main():
    stack = "{}))))"
    ex1 = Stack()
    print(ex1.if_balanced(stack))

if __name__ == '__main__':
    main()