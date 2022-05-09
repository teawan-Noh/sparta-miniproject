from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

import boto3
from flask_cors import CORS
import os

application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})

client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta
# db = client.admin

# HTML 화면 보여주기
@application.route('/')
def home():
    return render_template('index.html')

@application.route('/allList', methods=['GET'])
def list_all():
    all_list = list(db.tour.find({},{'_id':False}))
    # print(all_list)

    return jsonify({'all_list':all_list})

@application.route('/listByTitle', methods=['GET'])
def list_search():
    search_value = request.args.get('val')

    searched_list = list(db.tour.find({'title': {'$regex':search_value}},{'_id':False}))

    return jsonify({'searched_list':searched_list})

@application.route('/api/like', methods=['POST'])
def like_tour():
    title_receive = request.form['title_give']
    target_tour = db.tour.find_one({'title': title_receive})
    current_like = target_tour['like']
    new_like = current_like + 1
    db.tour.update_one({'title':title_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요 완료!'})

@application.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']
    s3 = boto3.client('s3',
                      aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                      aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
                      )
    s3.put_object(
        ACL="public-read",
        Bucket=os.environ["BUCKET_NAME"],
        Body=file,
        Key=file.filename,
        ContentType=file.content_type
    )
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    application.debug = True
    application.run()

# if __name__ == '__main__':
#     application.run('0.0.0.0', port=5000, debug=True)