#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import requests
import numpy as np
import csv
from flask import Flask, request

import mori
import luis2vec
import luisapp

app = Flask(__name__)
env = os.environ


@app.route('/messages', methods=['POST'])
def messages():
    if is_request_valid(request):
        # requestを変数に代入
        body = request.get_json(silent=True)
        companyId = body['companyId']
        msgObj = body['message']
        groupId = msgObj['groupId']
        messageText = msgObj['text']
        userName = msgObj['createdUserName']

        database = load_json()

        if messageText in database.keys():
            lenAr = len(database[messageText]["WR"])
            ars = database[messageText]["WR"][lenAr - 1]["AR"]
            hoursUser = database[messageText]["WR"][lenAr - 1]["working_time_diff_min"]
            print lenAr
            print ars
            print hoursUser
            send_message(companyId, groupId,
                         messageText.decode('utf-8') + "さんの労働時間は".decode('utf-8') + str(hoursUser).decode(
                             'utf-8') + "分".decode('utf-8'))
            vec = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
            for ar in ars:
                jsonAr = luisapp.getAppJsonByParam(ar)
                vec = vec + np.array(luis2vec.getVector(jsonAr), dtype=float)
            hourStd = call_tensor(vec)
            battlePower = 500000 * (float(hourStd) / float(hoursUser))
            send_message(companyId, groupId,
                         "先週のタスクの標準的な労働時間は".decode('utf-8') + str(int(float(hourStd))).decode('utf-8') + "分".decode(
                             'utf-8') + "\n".decode('utf-8') + messageText.decode('utf-8') + "さんの戦闘力は".decode(
                             'utf-8') + str(int(battlePower)).decode('utf-8') + "です！".decode('utf-8'))
        else:
            print "not exist"
            send_message(companyId, groupId, "存在しません".decode('utf-8'))

        return "OK"
    else:
        return "Request is not valid."


# Check if token is valid.
def is_request_valid(request):
    validationToken = env['CHIWAWA_VALIDATION_TOKEN']
    requestToken = request.headers['X-Chiwawa-Webhook-Token']
    return validationToken == requestToken


#
def load_json():
    f = open('./data/database.json', 'r')
    database = json.load(f)
    return database


# 同ユーザー名のcsvを読み込み最終行を返却
def load_user_data(fileName):
    with open('data/' + fileName) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        data = []
        for row in spamreader:
            data = row  # 最終行を読み込むいい方法が他にあるかも
        return data


# Call tensorFlow
def call_tensor(vec):
    hours = mori.main_tensor(vec)
    return str(hours[0][0])


# Send message to Chiwawa server
def send_message(companyId, groupId, message):
    url = 'https://{0}.chiwawa.one/api/public/v1/groups/{1}/messages'.format(companyId, groupId)
    headers = {
        'Content-Type': 'application/json',
        'X-Chiwawa-API-Token': env['CHIWAWA_API_TOKEN']
    }
    content = {
        'text': message.encode('utf-8')
    }
    requests.post(url, headers=headers, data=json.dumps(content))


if __name__ == '__main__':
    app.run(host='', port=80, debug=True)

    # import sys
    # if len(sys.argv)>1:
    #     load_user_data(sys.argv[1])
