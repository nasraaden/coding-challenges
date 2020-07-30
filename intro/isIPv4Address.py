'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
'''


def isIPv4Address(inputString):
    inputString = inputString.split('.')
    if len(inputString) != 4:
        return False
    for i in range(len(inputString)):
        if inputString[i].isnumeric() == False or inputString[i] == '':
            return False
        if int(inputString[i]) < 10 and len(inputString[i]) > 1:
            return False
        if int(inputString[i]) < 0 or int(inputString[i]) > 255:
            return False
    return True


inputString = '172.16.254.1'

print(isIPv4Address(inputString))
