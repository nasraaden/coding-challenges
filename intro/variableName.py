'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.
'''


def variableName(name):
    if name[0].isnumeric() or ' ' in name:
        return False
    return name.isalnum() or "_" in name


name = "var_1__Int"

print(variableName(name))
