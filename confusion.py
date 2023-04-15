# encoding=utf8
# -*- coding: utf-8 -*-
# author by heyujia
# 脚本将会用于对指定目录下的.h .m源码中的字符串进行转换
# 替换所有字符串常量为加密的char数组，形式((char[]){1, 2, 3, 0})

import importlib
import os
import re
import sys


# replace替换字符串为((char[]){1, 2, 3, 0})的形式，同时让每个字节与0xAA异或进行加密
# 当然可以不使用0xAA 使用其他的十六进制也行 例如0XBB、0X22、0X11
def replace(match):
    string = match.group(2) + '\x00'
    replaced_string = '((char []) {' + ', '.join(["%i" % ((ord(c) ^ 0xAA) if c != '\0' else 0) for c in list(string)]) + '})'
    return match.group(1) + replaced_string + match.group(3)


# obfuscate方法是修改传入文件源代码中用confusion_NSSTRING标记的所有字符串
# 使用replace函数对字符串进行异或转换
def obfuscate(file):
    with open(file, 'r') as f:
        code = f.read()
        f.close()
        code = re.sub(r'(confusion_NSSTRING\(|confusion_CSTRING\()"(.*?)"(\))', replace, code)
        code = re.sub(r'//#define ggh_confusion', '#define ggh_confusion', code)
        with open(file, 'w') as f:
            f.write(code)
            f.close()


# openSrcFile方法是读取源码路径下的所有.h和.m 文件
# 对每个文件执行obfuscate函数
def openSrcFile(path):
    print("混淆的路径为 "+ path)
    # this folder is custom
    for parent,dirnames,filenames in os.walk(path):
        #case 1:
        #        for dirname in dirnames:
        #            print((" parent folder is:" + parent).encode('utf-8'))
        #            print((" dirname is:" + dirname).encode('utf-8'))
        #case 2
        for filename in filenames:
            extendedName = os.path.splitext(os.path.join(parent,filename))
            if (extendedName[1] == '.h' or extendedName[1] == '.m'):
                print("处理源代码文件: "+ os.path.join(parent,filename))
                obfuscate(os.path.join(parent,filename))


#这里需要修改源码的路径为自己工程的文件夹名称
srcPath = '../EncryptedString'

if __name__ == '__main__':
    print("本脚本用于对源代码中被标记的字符串进行加密")

    if len(srcPath) > 0:
        openSrcFile(srcPath)
    else:
        print("请输入正确的源代码路径")
        sys.exit()
