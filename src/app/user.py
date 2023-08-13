'''
Author: magician 337558186@qq.com
Date: 2023-07-17 11:26:42
desc:
'''

from flask import Blueprint
from src.config.db_config import cur  # 数据库连接配置

# 创建蓝图
user_blue = Blueprint('user', __name__)


def data_format(result):
    '''
    description: 格式化查询数据；带有表头;将查询结果按字典 列表的方式输出
    return {*}
    '''    
    list_result = []
    for i in result:
        date_list = list(i)
        des = cur.description  # 获取表详情，字段名，长度，属性等
        table_head = [item[0] for item in des]  # 获取表头
        dict_result = dict(zip(table_head, date_list))  # 打包为元组的列表 再转换为字典
        list_result.append(dict_result)  # 将字典添加到list_result中
    return list_result


@user_blue.route('/users', methods=['get'])
def users():
    '''
    description: 获取用户信息
    return {*}
    '''
    sql = "select *  from userinfo"
    cur.execute(sql)
    result = cur.fetchall()
    return data_format(result)


"""
TODO 对于变量，我们需要使用 <> 
TODO <int:user_id>,这里用到了Flask自带的路由转换器 int,表示接收到的 user_id 是整数类型，
TODO 如果不加的话，那么就默认是 string 转换器。
"""
@user_blue.route('/<username>', methods=['get'])
def get_by_name(username: str = None):
    '''
    description: 根据用户名获取用户信息
    return {*}
    '''    
    sql = "SELECT * FROM userinfo WHERE username = ?" 
    params = (username,)
    cur.execute(sql,params)
    result = cur.fetchmany(1)   #! 一次查找1条
    result_list = data_format(result)
    if result:
        return {"user_id": result_list[0].get('id', 'unknown'), "username": result_list[0]["username"]}
    else:
        return {"error": "User not found"}

