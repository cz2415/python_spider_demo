# -*- coding:utf-8 -*-
from pip._vendor.distlib.compat import raw_input

while True:
    text = raw_input('Enter text[exit to quit]: ')
    if text != 'exit':
        print(text)
    else:
        break
print('bye')
