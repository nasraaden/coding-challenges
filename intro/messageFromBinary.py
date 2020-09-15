'''
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.
Assuming that your hunch is correct, decode the message.
'''


def messageFromBinaryCode(code):
    code = [code[i:i+8] for i in range(0, len(code), 8)]
    result = ''
    for i in range(len(code)):
        decimal = int(code[i], 2)
        symbol = chr(decimal)
        result += symbol
    return result
