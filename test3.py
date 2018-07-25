# coding: utf-8

import cx_Oracle

x=''

# 创建连接
connection = cx_Oracle.connect('hr', 'hr', 'localhost:1521/oracle')
# 创建游标
cursor = connection.cursor()

if cursor:
    cursor.execute('select * from sal_history')

    h = cursor.description

    title = [i[0] for i in h]

    # 格式化字符串
    g = lambda k: "%-8s" % k
    title = map(g, title)

    for i in title:
        x += str(i) + '   '

    print(x)
    print(h)