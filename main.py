# 导入模块
import requests
import json

url = "https://api.github.com/users/octocat"
response = requests.get(url)
data = json.loads(response.text)
print(data)
