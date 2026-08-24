# import os
# import sys
# from pathlib import Path
# from datetime import datetime
# import math
# from collections import Counter
# # print(math.sqrt(16))
# # print(math.ceil(5.0))
# # print(math.floor(5.0))
# # print(math.factorial(5))
# # print(datetime.now().date())
# # now = datetime.now()
# # print(now)
# # files=Path(".").glob("main.py")
# # for file in files:
# #     print(file)
# # print(sys.argv)
# arr=[1,2,3,4,4,5,6,7,8,9]
# print(Counter(arr))

import sqlite3
connection=sqlite3.connect("mydb.db")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(id integer primary key,name text,age integer)")

connection.commit()
connection.close()
