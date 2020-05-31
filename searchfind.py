# -*- coding: utf-8 -*-
import Couplet.server


# 查找文件
def find(resource):
    # 初始化
    response = ''
    f1 = open('data/dl-data/couplet/train/in.txt', 'r', encoding='UTF-8')
    f2 = open('data/dl-data/couplet/train/out.txt', 'r', encoding='UTF-8')
    i = 0
    j = 0
    z = 0
    for content in f1.readlines():
        i = i + 1
        content =''.join(content.split(' '))
        if i == 770491:
           content = content + '\n'
        if content == resource:
            z = 1
            break

    print(i)
    print(z)
    if z == 1:
        for content in f2.readlines():
            j = j + 1
            if j == i:
                response = content
                break
    print(j)
    response = ''.join(response.split(' '))
    return response
