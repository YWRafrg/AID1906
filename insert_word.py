import pymysql
import re

# 连接数据库
db = pymysql.connect(host='192.168.93.1',  # 替换为WSL中MySQL服务器的IP地址
                     port=3306,  # 如果MySQL服务器已更改了默认端口，需要更改此处的端口号
                     user='ywr',
                     password='123456',
                     database='dict',
                     charset='utf8')

f = open('dict.txt')
# 获取游标（操作数据库，执行sql语句）

cur = db.cursor()

sql = "insert into words (word,mean) values" \
      "(%s,%s)"
for line in f:
    # 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except:
        db.rollback()
#  data = f.readline()
# tmp = data.split(' ')
# word = tmp[0]
# mean = ' '.join(tmp[1:]).strip()
f.close()
cur.close()
db.close() 