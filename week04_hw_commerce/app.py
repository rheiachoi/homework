from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']

    orders = {
        'name': name,
        'count': count,
        'address': address,
        'phone': phone
    }

    db.orders.insert_one(orders)

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    orders= list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': '주문리스트를 확인해주세요', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)