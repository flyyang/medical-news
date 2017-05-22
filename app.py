import requests
import ast
import json
from config import wechat_conf
import simplejson
class WeChat(object):

    def __init__(self):
        self.corpid = wechat_conf["corpid"]
        self.corpsecret = wechat_conf["corpsecret"]
        self.party = wechat_conf["party"]
        self.agentid = wechat_conf["agentid"]
        self.token_url = wechat_conf["token_url"]
        self.msg_url = wechat_conf["msg_url"]

    def send(self, subject, msg):
        msg = self.normalize(msg)
        payload = {
            "touser": "",
            "toparty": self.party,
            "msgtype": "news",
            "agentid": self.agentid,
            "news": {
                "articles":
                    [
                        {
                            "title": subject, 
                            "description": msg, 
                            "url": "",
                            "picurl": ""
                        }
                    ]
                },
            "safe": "0"
        }
        
        r = requests.post(self.msg_url + "?access_token=" + self.get_token(),
                          data=simplejson.dumps(payload, ensure_ascii=False).encode('utf8'),
                          headers={'Content-type':'application/json', 'charset': 'utf-8'})
        return r
    
    def get_token(self):
        payload = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        r = requests.get(self.token_url, params=payload)
        data = ast.literal_eval(r.text)
        return data["access_token"]

    def normalize(self, broker_message):
        msg = broker_message
        return msg


wc = WeChat()

wc.send('hello','world')
