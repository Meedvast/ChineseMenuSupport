# 导入 re 模块
import os
import re
import shutil


# 创建一个函数来替换文本
def replace_text(file, search_text, replace_text_):
    # 以读写模式打开文件
    with open(file, 'r+') as f:
        # 读取文件数据并将其存储在文件变量中
        file = f.read()

        # 用文件数据中的字符串替换模式
        file = re.sub(search_text, replace_text_, file)

        # 设置位置到页面顶部插入数据
        f.seek(0)

        # 在文件中写入替换数据
        f.write(file)

        # 截断文件大小
        f.truncate()

    # 返回“文本已替换”字符串


def match_then_insert(filename):
    """
    :param filename: 要操作的文件
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        lines = f.readlines()
        menu = ''
        i = 0
        for line in lines:
            i += 1
            if re.search(r'\(\w{2}\.', line):
                language = re.search(r'\(\w{2}\.', line).group()
            if re.search(r'else if \(\w*\.equals\(\w*\.\w\)\)', line):
                menu = re.search(r'else if \(\w*\.equals\(\w*\.\w\)\)', line).group()
                continue
            if len(menu) != 0:
                line = re.sub(r'\n', r'', line)
                line = re.sub(r'new\s\w*', r'new zm', line)
                zm = re.sub(r'\s\w*\.\w?', language + 'J', line)
                menu = re.sub(r'\(\w{2}\.\w?', language + 'J', menu)
                zm_menu = menu + ' {\n' + zm + '\n\t\t\t}'
                lines[i] = re.sub(r'}', r'} ' + zm_menu, lines[i])
                lines[1] = re.sub(r'\n', ' import zm;\n', lines[1])
                file = open(filename, 'w')
                file.writelines(lines)
                file.close()
                break


def get_eng_menu(filename):
    with open(filename, mode='r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'\(\w{2}\.', line):
                language = re.search(r'\(\w{2}\.', line).group()
                break
        for line in lines:
            eng_language = re.sub(r'\(', '', language) + 'a'
            if re.search(eng_language, line):
                eng_menu = re.search(r'new \w{1,2}', line).group().split()[1]
                break
    return eng_menu


