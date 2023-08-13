"""
@Time ： 2023/5/25 16:36
@Auth ： 植树的牧羊人
@desc : sqlite配置
"""
import sqlite3

# 数据库连接
conn = sqlite3.connect("./static/data/demo_flask.db", timeout=10, check_same_thread=False)
cur = conn.cursor()
