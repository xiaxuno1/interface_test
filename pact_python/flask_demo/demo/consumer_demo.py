import requests
from flask import Flask, jsonify

app = Flask(__name__)


# 定义了消费者接口，接口支持GET方法，接口路径为/consumer01
@app.route('/consumer01', methods=["GET"])
def get_demo():
    # 请求生产者，获取响应结果，并转为json格式
    res = requests.get('http://127.0.0.1:8000/provider').json()
    print(res)
    # 拼接get_demo的接口响应结果内容。
    result = {
        "code": 0,
        "msg": "ok",
        "data": res
    }
    print(result)
    # 结果返回
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
