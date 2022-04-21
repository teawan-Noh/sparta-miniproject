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
    print(all_list)
    # print('avc')
    return jsonify({'all_list':all_list})
    # return jsonify({'all_list':'avc'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)