'''
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.
Return an array of names that will be given to the files.
'''


def fileNaming(names):
    names_dict = {}
    result = []
    for i in range(len(names)):
        if names[i] not in names_dict:
            names_dict[names[i]] = 1
            result.append(names[i])
        else:
            temp = names[i] + '('+str(names_dict[names[i]])+')'
            while temp in names_dict:
                names_dict[names[i]] += 1
                temp = names[i] + '(' + str(names_dict[names[i]]) + ')'
            names_dict[names[i]] += 1
            names_dict[temp] = 1
            result.append(temp)
    return result
