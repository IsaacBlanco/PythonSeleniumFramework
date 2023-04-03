# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi():
    text = """,な周歩廊そ
    ,る囲い下の
    ,だのてにょ
    ,る邪は広う
    ,う魔 がに
    , に っ 
    ,   て """
    # Split the text into lines
    lines = text.split('\n')
    flines = []
    for i in lines:
        if i:
            row = i.lstrip()
            flines.append(row)
    print(flines)

    transpose_text = []
    for i in range(len(flines)):
        row = ''
        for r, line in enumerate(flines):
            row += line[-1:]
            flines[r] = line[:-1]

        transpose_text.append(row)

    for line in transpose_text:
        print(line)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
