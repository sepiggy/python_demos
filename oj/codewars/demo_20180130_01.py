#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def spin_words(sentence):
    word_list = sentence.split(' ')
    result = ''
    for i in range(len(word_list)):
        if len(word_list[i]) < 5:
            if not i == len(word_list) - 1:
                result += word_list[i] + ' '
            else:
                result += word_list[i]
        if len(word_list[i]) >= 5:
            new_word = ''
            for j in range(len(word_list[i]) - 1, -1, -1):
                new_word += word_list[i][j]
            if not i == len(word_list) - 1:
                result += new_word + ' '
            else:
                result += new_word

    return result


if __name__ == '__main__':
    r = spin_words('Welcome')
    print(len(r))
