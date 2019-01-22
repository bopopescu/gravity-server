import requests
import simplejson as json

url = 'https://gcm-http.googleapis.com/gcm/send'

headers = {'Content-Type': 'application/json',
           'Authorization':'key=AIzaSyDbUSb5tkJZCKD2_S34V6-V_Ja67G9B0-Y'}

payload = {'to': '/topics/gravity',
           "data": {
                "message": "This is a GCM Topic Message!",
                }
           }

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.headers)
print(r.text)


