"""
This script pulls the font awesome spec from their repo on github,
then generates a python version of it.

Much of this script was inspired by fontawesome-markdown:
https://github.com/bmcorser/fontawesome-markdown/blob/master/scripts/update_icon_list.py
"""

import yaml
import requests
import sys


REVISION = 'master'

URI = ('https://raw.githubusercontent.com'
       '/FortAwesome/Font-Awesome/%s/src/icons.yml' % REVISION)

CONFIG_URI = ('https://raw.githubusercontent.com'
    '/FortAwesome/Font-Awesome/%s/_config.yml' % REVISION)

INDENT = ' ' * 2

def main():
    icons_list = yaml.load(requests.get(URI).text)['icons']
    version = yaml.load(requests.get(CONFIG_URI).text)['fontawesome']['version']

    out = sys.stdout

    out.write("# This file was generated automatically by fontawesome-python\n")
    out.write("# It contains the icon set from: https://github.com/FortAwesome/Font-Awesome\n")
    out.write("# The content is licensed under the SIL OFL 1.1: http://scripts.sil.org/OFL\n")
    out.write('\n')
    out.write('VERSION = \'%s\'\n' % version)
    out.write('\n')
    out.write('icons = {\n')
    for icon in icons_list:
        # dict entry with character code
        entry = "'%s': '\\u%s'," % (icon['id'], icon['unicode'])
        indent_to = 50
        entry += ' ' * (indent_to - len(entry)) # pad
        # comment with font awesome icon
        entry += '# %s' % chr(int(icon['unicode'], 16))
        out.write(INDENT + entry + '\n')

    out.write('}\n')


if __name__ == '__main__':
    main()
