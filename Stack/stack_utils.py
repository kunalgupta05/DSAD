from Stack.stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_parenthesis_balanced(input_string):
    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(input_string) and is_balanced:
        paren = input_string[index]
        if paren in "([{":
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                top = stack.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if stack.is_empty() and is_balanced:
        return True
    else:
        return False


def reverse_string(stack: Stack, input_str: str):
    for char in input_str:
        stack.push(char)

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


def convert_int_to_bin(stack: Stack, dec_num: str):
    if not dec_num.isnumeric():
        return "Please enter a valid string with integer value"

    dec_num = int(dec_num)

    if dec_num == 0:
        return 0

    binary_str = ""

    while dec_num > 0:
        dec_num, remainder = divmod(dec_num, 2)
        stack.push(remainder)

    while not stack.is_empty():
        binary_str += str(stack.pop())

    return binary_str

