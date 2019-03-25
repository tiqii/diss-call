from flask import render_template, request, jsonify
from . import main


@main.route('/', methods=["GET"])
def index():
    """ 
    获取需要diss的电话号码，做diss请求后返回diss状态
    """
    # 获取需要diss的号码
    phone_num = request.args['phone_num']

    # 这里做diss操作
    # TODO: 接入diss操作

    # 返回
    res = {"status": 201, "msg": "success", "data": {"phone": phone_num}}
    return jsonify(res)
