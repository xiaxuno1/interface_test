import requests
from flask import Flask, jsonify

app = Flask(__name__)


# 生产者的接口信息，支持POST与GET请求，接口路径是/provider
@app.route('/provider', methods=['POST', 'GET'])
def send_demo():
    data = {
        "name": "xuzhu",
        "age": 18
    }
    # 将返回值定义为JSON格式的形态进行返回
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
