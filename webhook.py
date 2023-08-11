import requests
import json
class Webhook:
    def __init__(self, url):
        self.url = url
    
    def sendmsg(self, content):
        data = {
            "content": f"{content}"
        }
        r=requests.post(self.url, data=json.dumps(data), headers={"Content-Type": "application/json"})