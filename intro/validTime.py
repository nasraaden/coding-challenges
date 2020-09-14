'''
Check if the given string is a correct time representation of the 24-hour clock.
'''


def validTime(time):
    time = time.split(':')
    for i in range(len(time)):
        if int(time[0]) > 23:
            return False
        if int(time[1]) > 59:
            return False

    return True
