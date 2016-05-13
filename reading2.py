#!/usr/local/bin/python
#coding=utf-8

#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
#使用 Python 如何生成 200 个激活码（或者优惠券）？

import uuid


def create_code(num, length):
#生成”num“个激活码，每个激活码含有”length“位
    result = []
    while True: #to create a infinite loop.
        uuid_id = uuid.uuid1() #UUID stands for universal unique identifier.
        temp = str(uuid_id).replace('-', '')[:length] 
        if not temp in result: # Basically it will put temp into result
            result.append(temp) 
            			
        if len(result) == num:
            break
    return result

print create_code(200, 20)

