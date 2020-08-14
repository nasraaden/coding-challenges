'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";

'''


def reverseInParentheses(inputString):
    string_list = list(inputString)
    stack = []
    new_string = ""

    for i in range(len(string_list)):
        if string_list[i] == '(':
            stack.append(i)
        elif string_list[i] == ')':
            j = stack.pop()
            string_list[j:i] = string_list[i:j:-1]

    for i in range(len(string_list)):
        if string_list[i] != ')':
            new_string += string_list[i]

    return new_string
