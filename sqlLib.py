import sqlite3

import os

DBName = 'static/DB.db'
#
# conn = sqlite3.connect(DBName)
# c = conn.cursor()



# c.execute('''
# CREATE TABLE PW(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# EMAIL TEXT NOT NULL ,
# PASSWORD TEXT NOT NULL
# );
# ''')
# conn.commit()

# cursor = c.execute("SELECT EMAIL, PASSWORD FROM PW")
# for row in cursor:
#     emailDB = row[0]
#     passwordDB = row[1]
#     print(emailDB)
#     print(passwordDB)

# c.execute("INSERT INTO PW (EMAIL,PASSWORD) VALUES ('1015323766@qq.com','a123456s')")
# conn.commit()


# conn.close()
try:
    os.mkdir(r'static/user/{}'.format(123))
except FileExistsError as e:
    print(e)

s = ''
l =[]
n = 0
walk = os.walk(r'static')
root_list = []
root_list_len = []
root_list_len_range = []
root_list_split = []

for root, dirs, files in walk:
    print(root)
    print(dirs)
    print(files)
    root_list.append(root)
    break
    #print(files)
print(root)
#
# for i in root_list:
#     root_list_len.append(len(str(i).split('\\')))
#     root_list_split.append(str(i).split('\\'))
#
# for i in root_list_len:
#     root_list_len_range.append(list(range(i-1)))
#
# root_list_num = list(range(len(root_list)))
# print(root_list)
# print(root_list_len)
# print(root_list_len_range)
# print(root_list_split)
# print(root_list_num)
#
#
#
#
# s_mode = ''
# for i in root_list_num:
#     if root_list_len[i] == 1:
#         s_mode += root_list[i]
#         s_mode += '\n'
#     else:
#         for _ in root_list_len_range[i]:
#             s_mode += '  '
#         s_mode += '+'
#         temp = str(root_list[i]).split('\\')
#         s_mode += temp[-1]
#         s_mode += '\n'
#
# print(s_mode)

# for root,dirs,files in walk:
#     print('file')
#     for f in files:
#         print(os.path.join(root,f))
#     print('*********************************')
#     print('path')
#     for d in dirs:
#         print(os.path.join(root,d))
#
#     print('---------------------------------')
#
# list_1 = [[11],[[12],[13]]]
# for i in list_1:
#     print(i)
