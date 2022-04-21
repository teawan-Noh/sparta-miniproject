from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/allList', methods=['GET'])
def list_all():
    all_list = list(db.tour.find({},{'_id':False}))

    return jsonify({'all_list':all_list})

def like_tour():
    title_receive = request.form['title_give']
    target_tour = db.tour.find_one({'title': title_receive})
    current_like = target_tour['like']
    new_like = current_like + 1
    db.tour.update_one({'title':title_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)