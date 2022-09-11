import pymysql

DBHOST = '47.98.53.127'
DBUSER = 'cx'
DBPASS = '123456'
DBNAME = 'cx'
initData = ['1', '1976756410', '我是一号', '12345678a', 'null']

try:
    # 数据库链接
    db = pymysql.connect(host=DBHOST, user=DBUSER,
                         password=DBPASS, database=DBNAME)
    print('数据库成功连接')
    cur = db.cursor()
    # 创建表格
    cur.execute("DROP TABLE IF EXISTS User")
    sql = 'CREATE TABLE User(sid CHAR(50),Email CHAR(50),UserName CHAR(50),Password CHAR(50),ImgUrl CHAR(50))'
    cur.execute(sql)
    # 插入数据
    sql = 'INSERT INTO User(sid,Email,UserName,Password,ImgUrl)VALUE(%s,%s,%s,%s,%s)'
    # for data in initData:
    value = tuple(initData)
    cur.execute(sql, initData)
    db.commit()
    print("表格创建成功")
    # 向表格插入一条数据
except pymysql.Error as e:
    print('数据库连接失败')
    print(e)
    db.rollback()
# 关闭数据库
db.close()
