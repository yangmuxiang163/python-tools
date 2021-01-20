# 对并行查找多机合并后的日志，按时间排序。日期格式如下：
# INFO 2021-01-19 22:00:00.207: ... 

import os
import sys
import regex as re
import datetime
 
if len(sys.argv) < 2:
    fp = os.sys.stdin
    pass
else:
    fp = open(sys.argv[1])
    pass

a = []
pattern=r"(.*?) ([1-9][0-9]{3}-[01][0-9]-[01][0-9] [01][0-9]:[0-9][0-9]:[0-9][0-9]\.\d+)(.*)"
for line in fp.readlines(): # 遍历每一行
    mg = re.match(pattern, line, re.I)
    a.append(mg.groups())

fp.close()

a.sort(key=lambda x: datetime.datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S.%f'))
for i in a:
   print("{} {}{}".format(i[0], i[1], i[2]))
