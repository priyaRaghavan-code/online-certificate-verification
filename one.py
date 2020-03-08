import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/d7cb9568-7ef6-47ff-9acd-bc9c6885264c/LabelFile/'

data = {'file': open('002.jpg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('HNOd95k5USnXaqtM6nB4ZrK7hrb9MJED', ''), files=data)

f = open('file.txt', 'w')
f.write(response.text)
# print(response.text)