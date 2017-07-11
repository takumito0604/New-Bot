from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import os
import random
import sys
sys.path.append('/Users/takumito0604/python/katakurushi_bot/bot')
from load_serif import load_serif

# Create your views here.
REPLY_ENDPOINT='https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN=os.getenv("access_token")
HEADER={
    "Content-Type": "application/json",
    "Authorization": "Bearer {ACCESS_TOKEN}"
  }

def reply_text(reply_token, text):
    reply=random.choice(katakurushi_aisatsu)
    payload={
          "replyToken":reply_token,
          "message":[
          {
            "type":"text",
            "text": reply
          }
        ]
    }
    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
    return reply

def index(request):
    return HttpResponse("this is bot API.")

def callback(request):
    reply=""
    request_json=json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token=e['replyToken']
        message_type=e['message']['type']

        if message_type=='text':
            text=e['message']['text']
            reply+=reply_text(reply_token,text)
    return HttpResponse(reply)
