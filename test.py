import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8')
cursor = db.cursor()

cursor.execute("drop table if exists Recommended")

sql = """
create table Recommended (
film varchar(80) not null,
rating DECIMAL (7, 4) not null )
"""
cursor.execute(sql)

# a = "hhhhjhjhjhjhjhjhjh"
# b = 95.1564845544


# sql = 'insert into Recommended (`film`,`rating`) values("%s","%f")'%(a,b)
# cursor.execute(sql)
# db.commit()