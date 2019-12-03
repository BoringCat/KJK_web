#! /usr/bin/env python3

from random import randint as 随机整数, randrange as 随机范围

gbk文字编码段 = [
    ((176, 247), (161, 254)),   # B0-F7, A1-FE
    ((129, 160), (64, 126)),    # 81-A0, 40-7E
    ((129, 160), (128, 254)),   # 81-A0, 80-FE
    ((170, 254), (64, 126)),    # AA-FE, 40-7E
    ((170, 254), (128, 160))    # AA-FE, 80-FE
]

gbk符号编码段 = [
    ((161, 169), (161, 254)),   # A1-A9, A1-FE
    ((168, 169), (64, 126)),    # A8-A9, 40-7E
    ((168, 169), (128, 160))    # A8-A9, 80-FE
]

def 生成锟斤拷(字节长度 = 8, 包括符号 = False, 返回文字 = False):
    返回的文字 = ''
    gbk范围 = gbk文字编码段.copy()
    if 包括符号:
        gbk范围 += gbk符号编码段.copy()
    for _ in range(0,字节长度,2):
            第一位, 第二位 = gbk范围[随机整数(0,len(gbk范围)-1)]
            while True:
                try:
                    返回的文字 += bytes([ 随机范围(*第一位), 随机范围(*第二位)]).decode('GBK')
                    break
                except UnicodeDecodeError:
                    pass
    return 返回的文字 if 返回文字 else 返回的文字.encode('GBK')

if __name__ == "__main__":
    print(生成锟斤拷(字节长度 = 512, 返回文字 = True, 包括符号 = False))