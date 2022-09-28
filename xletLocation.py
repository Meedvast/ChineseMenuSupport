import os
import usage
import shutil
import re


def get_menu_class(path):
    menu_class = []
    with open(path, mode='r', encoding='UTF-8') as f:
        lines = f.readlines()
        menu_class.append(re.search(r'private \w{1,2}', lines[1]).group().split()[1])
        for line in lines:
            if re.search(r'new Integer\(\d*\)', line):
                menu_class.append(re.search(r'new [a-z]{1,2}', line).group().split()[1])
    return menu_class


def replace_xlet(path, new_path):
    file_name = ''
    title_path = path + '/title'
    files = os.listdir(title_path)
    xlet_files = []
    for name in files:
        if 'Xlet' in name:
            xlet_files.append(name)
        for file_name in xlet_files:
            if 'java' in file_name:
                break
    usage.match_then_insert(title_path + '/' + file_name)
    eng_menu = usage.get_eng_menu(title_path + '/' + file_name)
    menu_class = get_menu_class(path + '/' + eng_menu + '.java')
    if not os.path.exists(new_path + '/title'):
        os.mkdir(new_path + '/title')
    shutil.copy(title_path + '/' + file_name, new_path + '/title/' + file_name)
    shutil.copy(path + '/' + eng_menu + '.java', new_path + '/zm.java')
    usage.replace_text(new_path + '/zm.java', usage.get_eng_menu(title_path + '/' + file_name), 'zm')
    i = 0
    picture_class = ''
    for file in menu_class:

        if i == 0:
            picture_class = file
            shutil.copy(path + '/' + file + '.java', new_path + '/zp.java')
            usage.replace_text(new_path + '/zp.java', file, 'zp')
            usage.replace_text(new_path + '/zp.java', 'Eng', 'Zho')
            i += 1
        else:
            shutil.copy(path + '/' + file + '.java', new_path + '/z' + chr(96 + i) + '.java')
            usage.replace_text(new_path + '/z' + chr(96 + i) + '.java', file, 'z' + chr(96 + i))
            usage.replace_text(new_path + '/z' + chr(96 + i) + '.java', picture_class, 'zp')
            i += 1
    j = 0
    for file in menu_class:
        if j == 0:
            usage.replace_text(new_path + '/zm.java', file, 'zp')
            j += 1
        else:
            usage.replace_text(new_path + '/zm.java', file, 'z' + chr(96 + j))
            j += 1
