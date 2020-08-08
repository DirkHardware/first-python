# print(dir())
# Shows us everything in the implicitly imported __builtins__ module
# print(dir(__builtins__))
# for m in dir(__builtins__):
#     print(m)

import shelve

# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)
#

# help(shelve)

import webbrowser

# webbrowser.open('https://www.google.com')
firefox = webbrowser.get(using='firefox')
firefox.open_new('https://www.google.com')