"""
注册登录模拟
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='192.168.93.1',  # 替换为WSL中MySQL服务器的IP地址
                     port=3306,  # 如果MySQL服务器已更改了默认端口，需要更改此处的端口号
                     user='ywr',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 获取游标（操作数据库，执行sql语句）

cur = db.cursor()


# 注册
def register():
    name = input("用户名:")
    passwd = input("密码:")
    # 判断用户名是否重复
    sql = "select * from user where name='%s'" % name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (name,passwd)" \
              "values (%s,%s)"
        cur.execute(sql, [name, passwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False


def login():
    name = input("用户名:")
    passwd = input("密码:")
    sql = "select * from user " \
          "where name='%s' and passwd='%s'" % (name, passwd)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True


while True:
    print("""===================
            1.注册           2.登录
             ===================
    
    """)
    cmd = input("输入命令:")
    if cmd == '1':
        #     执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        #  执行登录
        if login():
            print("登录成功")
        else:
            print("登录失败")

    else:
        print("我做不到啊")

# 关闭数据库

cur.close()
db.close()
