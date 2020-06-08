def string_remove(str, letter):
    '''
    移除一个字符串的某个字母
    :param str:
    :param letter:
    :return:
    '''
    x = str.index(letter)
    return str[:x] + str[x+1:]