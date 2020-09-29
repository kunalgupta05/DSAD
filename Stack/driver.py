from Stack import stack_utils, stack

# Balance the string
print(stack_utils.is_parenthesis_balanced('[({'))
print(stack_utils.is_parenthesis_balanced('[({})]'))
print(stack_utils.is_parenthesis_balanced('[({]})'))


# Reverse the string
stack_1 = stack.Stack()
input_str = "!evitacudE ot emocleW"
print(stack_utils.reverse_string(stack_1, input_str))


# Binary equivalent of a decimal number
stack_2 = stack.Stack()
input_str = "23"
print(stack_utils.convert_int_to_bin(stack_2, input_str))
